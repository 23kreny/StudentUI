import dataclasses
import datetime
import json
from contextlib import contextmanager
from enum import Enum

from bakalib.core import Client
from bakalib.extra import Municipality
from bakalib.modules import Grades, Timetable
from bakalib.utils import BakalibError
from PySide2 import QtCore, QtGui, QtWidgets

from . import paths, version
from .ui_grades import Ui_gradesWindow
from .ui_login import Ui_loginDialog
from .ui_selector import Ui_selectorWindow
from .ui_timetable import Ui_timetableWindow


def handler(msg_type, msg_log_context, msg_string):
    pass


QtCore.qInstallMessageHandler(handler)


@contextmanager
def wait_cursor():
    try:
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor((QtCore.Qt.WaitCursor)))
        yield
    finally:
        QtWidgets.QApplication.restoreOverrideCursor()


class LoginDialog(QtWidgets.QDialog):
    login_send_client = QtCore.Signal(Client)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)

        self.clear()

        self.ui.showpassBox.clicked.connect(self.view_pass_handler)
        self.ui.pushLogin.clicked.connect(self.login_handler)

    def clear(self):
        self.ui.pushLogin.setEnabled(True)
        self.ui.rememberBox.setChecked(False)
        self.ui.showpassBox.setChecked(False)

        self.ui.cityCombo.clear()
        self.ui.schoolCombo.clear()
        self.ui.lineUser.clear()
        self.ui.linePass.clear()
        self.view_pass_handler()

        self.municipality = Municipality()

        self.ui.cityCombo.clear()
        self.ui.cityCombo.addItems(
            [city.name for city in self.municipality.municipality().cities]
        )
        self.ui.cityCombo.currentIndexChanged.connect(self.select_city_handler)
        self.select_city_handler()
        self.select_school_handler()

    def select_city_handler(self):
        self.ui.schoolCombo.clear()
        self.ui.schoolCombo.addItems(
            [
                school.name
                for school in self.municipality.municipality()
                .cities[self.ui.cityCombo.currentIndex()]
                .schools
            ]
        )
        self.ui.schoolCombo.currentIndexChanged.connect(self.select_school_handler)

    def select_school_handler(self):
        self.domain = (
            self.municipality.municipality()
            .cities[self.ui.cityCombo.currentIndex()]
            .schools[self.ui.schoolCombo.currentIndex()]
            .domain
        )

    def view_pass_handler(self):
        shown = QtWidgets.QLineEdit.EchoMode.Normal
        hidden = QtWidgets.QLineEdit.EchoMode.Password
        if self.ui.showpassBox.isChecked():
            self.ui.linePass.setEchoMode(shown)
        else:
            self.ui.linePass.setEchoMode(hidden)

    def login_handler(self):
        self.ui.pushLogin.setDisabled(True)
        try:
            username = self.ui.lineUser.text()
            password = self.ui.linePass.text()
            with wait_cursor():
                user = Client(username=username, domain=self.domain)
                user.login(password=password)
            if self.ui.rememberBox.isChecked():
                paths.auth_file.write_text(
                    json.dumps(
                        {
                            "username": user.username,
                            "domain": user.domain,
                            "perm_token": user.perm_token,
                        }
                    )
                )
            self.login_send_client.emit(user)
        except BakalibError as error:
            QtWidgets.QMessageBox.warning(None, "Error", f"{error}")
            self.ui.pushLogin.setEnabled(True)


class SelectorWindow(QtWidgets.QMainWindow):
    send_client = QtCore.Signal(Client)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.ui = Ui_selectorWindow()
        self.ui.setupUi(self)

        self.login = LoginDialog()

        if not paths.auth_file.is_file():
            self.login.login_send_client.connect(self.run)
            self.login.show()
        else:
            auth_file = json.loads(paths.auth_file.read_text())
            client = Client(username=auth_file["username"], domain=auth_file["domain"],)
            self.run(client, auth_file["perm_token"])

    def run(self, client: Client, perm_token: str = None):
        self.login.close()
        if perm_token:
            client.login(perm_token=perm_token)
        self.show()

        self.timetable_window = TimetableWindow(client=client)
        self.grades_window = GradesWindow(client=client)
        # self.absence_window = AbsenceWindow(client=client)

        self.ui.pushTimetable.clicked.connect(lambda: self.timetable_window.show())
        self.ui.pushGrades.clicked.connect(lambda: self.grades_window.show())
        self.ui.pushAbsence.clicked.connect(
            lambda: QtWidgets.QMessageBox.information(self, "WIP", "Něco tu chybí")
        )
        self.ui.pushLogout.clicked.connect(self.logout)

        self.update_info(client.info())

    def update_info(self, info):
        self.ui.labelName.setText(info.name.rstrip(", {}".format(info.class_)))
        self.ui.labelClass.setText(info.class_)
        self.ui.labelSchool.setText(info.school)

    def logout(self):
        paths.auth_file.unlink()
        self.login.clear()
        self.login.open()
        self.close()


class TimetableWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, client: Client = None):
        super().__init__(parent=parent)

        self.ui = Ui_timetableWindow()
        self.ui.setupUi(self)

        self.ui.Timetable.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )

        self.timetable = Timetable(client)

        self.ui.pushNext.clicked.connect(self.next)
        self.ui.pushPrev.clicked.connect(self.prev)
        self.ui.Timetable.cellClicked.connect(self.cell_click)

        self.build_timetable(self.timetable.this_week())

    def next(self):
        with wait_cursor():
            self.build_timetable(self.timetable.next_week())

    def prev(self):
        with wait_cursor():
            self.build_timetable(self.timetable.prev_week())

    def build_timetable(self, timetable):
        self.ui.Timetable.setRowCount(len(timetable.days))
        self.ui.Timetable.setColumnCount(len(timetable.headers))

        for column in range(self.ui.Timetable.columnCount()):
            for row in range(self.ui.Timetable.rowCount()):
                self.ui.Timetable.setSpan(row, column, 1, 1)

        self.ui.Timetable.setVerticalHeaderLabels(
            [
                "{}\n{}".format(
                    day.abbr,
                    datetime.datetime.strftime(
                        datetime.datetime.strptime(day.date, "%Y%m%d"), "%x"
                    ),
                )
                for day in timetable.days
            ]
        )
        self.ui.Timetable.setHorizontalHeaderLabels(
            [
                "{}\n{} - {}".format(header.caption, header.time_begin, header.time_end)
                for header in timetable.headers
            ]
        )

        self.ui.menuWeek.setTitle(timetable.cycle_name.capitalize())

        for i, day in enumerate(timetable.days):
            for x, lesson in enumerate(day.lessons):
                if lesson.type == "X" or lesson.type == "A":
                    if lesson.change_description:
                        item = QtWidgets.QTableWidgetItem(lesson.name)
                        item.setBackground(QtGui.QColor(255, 0, 0))
                        item.details = lesson
                    elif lesson.holiday:
                        item = QtWidgets.QTableWidgetItem(lesson.holiday)
                        item.setBackground(QtGui.QColor(99, 151, 184))
                        item.setTextAlignment(1)
                        self.ui.Timetable.setSpan(
                            i, x, 1, self.ui.Timetable.columnCount()
                        )
                    else:
                        item = QtWidgets.QTableWidgetItem("")
                else:
                    item = QtWidgets.QTableWidgetItem(
                        "{}\n{}\n{}".format(
                            lesson.abbr, lesson.teacher_abbr, lesson.room_abbr
                        )
                    )
                    if lesson.change_description:
                        item.setBackground(QtGui.QColor(255, 0, 0))
                    item.details = lesson
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.Timetable.setItem(i, x, item)

        for column in range(self.ui.Timetable.columnCount()):
            self.ui.Timetable.setColumnWidth(column, 88)
        for row in range(self.ui.Timetable.rowCount()):
            self.ui.Timetable.setRowHeight(row, 64)

    def cell_click(self, row, col):
        try:
            item = self.ui.Timetable.item(row, col).details
            details = [
                item.name,
                item.theme,
                item.teacher,
                item.room if item.room else item.room_abbr,
                item.change_description if item.change_description else None,
            ]
            details = [detail for detail in details if detail is not None]
            QtWidgets.QMessageBox.information(self, "Detaily", "\n".join(details))
        except AttributeError:
            print("No attributes")


class GradesWindow(QtWidgets.QMainWindow):
    class Sort(Enum):
        by_subject = 0
        by_date = 1

    def __init__(self, parent=None, client: Client = None):
        super().__init__(parent=parent)

        self.ui = Ui_gradesWindow()
        self.ui.setupUi(self)

        self.grades = Grades(client)

        self.ui.treeGrades.itemClicked.connect(self.item_click)
        self.ui.radioSubj.clicked.connect(self.sort_subject)
        self.ui.radioDate.clicked.connect(self.sort_date)

        self.build_tree()

    def sort_subject(self):
        self.build_tree(order=self.Sort.by_subject)

    def sort_date(self):
        self.build_tree(order=self.Sort.by_date)

    def build_tree(self, order: Enum = Sort.by_subject):
        self.ui.treeGrades.clear()
        self.ui.listDetails.clear()
        grades = self.grades.grades()

        if order == self.Sort.by_subject:
            for subject in grades.subjects:
                item_subject = QtWidgets.QTreeWidgetItem(self.ui.treeGrades)
                item_subject.setText(0, subject.name)
                for grade in subject.grades:
                    item_grade = QtWidgets.QTreeWidgetItem(item_subject)
                    item_grade.setText(0, grade.grade)
                    item_grade.details = grade
        elif order == self.Sort.by_date:
            unsorted_grades = []
            for subject in grades.subjects:
                for grade in subject.grades:
                    item_grade = QtWidgets.QTreeWidgetItem()
                    item_grade.setText(0, grade.grade)
                    item_grade.details = grade
                    unsorted_grades.append(item_grade)
            self.ui.treeGrades.addTopLevelItems(
                sorted(
                    unsorted_grades,
                    key=lambda x: datetime.datetime.strptime(x.details.date, "%y%m%d"),
                    reverse=True,
                )
            )
        else:
            raise ValueError("Wrong sorting type provided")

    def item_click(self, item):
        self.ui.listDetails.clear()
        try:
            item = item.details
            details = {
                "Subject": item.subject,
                "Caption": item.caption,
                "Description": item.description,
                "Note": item.note,
                "Weight": item.weight,
                "Date": datetime.datetime.strptime(item.date, "%y%m%d").strftime("%x")
                if item.date
                else None,
                "Date granted": datetime.datetime.strptime(
                    item.date_granted, "%y%m%d%H%M"
                ).strftime("%x, %X")
                if item.date_granted
                else None,
            }
            details = ["{}: {}".format(k, v) for k, v in details.items() if v]
            self.ui.listDetails.addItems(details)
        except AttributeError as e:
            print("No attributes")


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = SelectorWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
