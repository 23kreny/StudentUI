import datetime
import threading
from contextlib import contextmanager

import bakalib
from PySide2 import QtCore, QtGui, QtWidgets

import studentui.paths
from studentui.ui_login import Ui_loginDialog
from studentui.ui_selector import Ui_selectorWindow
from studentui.ui_timetable import Ui_timetableWindow


@contextmanager
def wait_cursor():
    try:
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor((QtCore.Qt.WaitCursor)))
        yield
    finally:
        QtWidgets.QApplication.restoreOverrideCursor()


class LoginDialog(QtWidgets.QDialog):
    login_send_client = QtCore.Signal(bakalib.Client)

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

        self.municipality = bakalib.Municipality()

        self.ui.cityCombo.clear()
        self.ui.cityCombo.addItems(
            [city.name for city in self.municipality.cities])
        self.ui.cityCombo.currentIndexChanged.connect(self.select_city_handler)
        self.select_city_handler()
        self.select_school_handler()

    def select_city_handler(self):
        self.ui.schoolCombo.clear()
        school_list = [
            school.name for school in self.municipality.cities[self.ui.cityCombo.currentIndex()].schools]
        self.ui.schoolCombo.addItems(school_list)
        self.ui.schoolCombo.currentIndexChanged.connect(
            self.select_school_handler)

    def select_school_handler(self):
        self.domain = self.municipality \
            .cities[self.ui.cityCombo.currentIndex()] \
            .schools[self.ui.schoolCombo.currentIndex()] \
            .domain

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
                user = bakalib.Client(
                    username=username, password=password, domain=self.domain)
            self.login_send_client.emit(user)
        except bakalib.BakalibError as error:
            QtWidgets.QMessageBox.warning(None, "Error", str(error))
            self.ui.pushLogin.setEnabled(True)


class TimetableWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, client=None):
        super().__init__(parent=parent)

        self.ui = Ui_timetableWindow()
        self.ui.setupUi(self)

        self.ui.Timetable.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)

        today = datetime.date.today()
        self.date = today + datetime.timedelta(days=-today.weekday(), weeks=1)

        self.client = client
        self.client.add_modules("timetable")

        self.ui.pushNext.clicked.connect(self.next)
        self.ui.pushPrev.clicked.connect(self.prev)
        self.ui.Timetable.cellClicked.connect(self.cell_click)

        self.thread = threading.Thread(target=self.client.timetable.this_week)
        self.thread.start()
        self.thread.join()

        self.next_thread = threading.Thread()
        self.prev_thread = threading.Thread()

        self.build_timetable(self.client.timetable.this_week())

        self.thread1 = threading.Thread(target=self.client.timetable.date_week, args=(
            self.date + datetime.timedelta(7),))
        self.thread2 = threading.Thread(target=self.client.timetable.date_week, args=(
            self.date - datetime.timedelta(7),))

        self.thread1.start()
        self.thread2.start()

    def next(self):
        self.date = self.date + datetime.timedelta(7)
        if self.next_thread.is_alive():
            with wait_cursor():
                self.next_thread.join()
        self.build_timetable(self.client.timetable.date_week(self.date))
        self.next_thread = threading.Thread(target=self.client.timetable.date_week, args=(
            self.date + datetime.timedelta(7),))
        self.next_thread.start()

    def prev(self):
        self.date = self.date - datetime.timedelta(7)
        if self.prev_thread.is_alive():
            with wait_cursor():
                self.prev_thread.join()
        self.build_timetable(self.client.timetable.date_week(self.date))
        self.prev_thread = threading.Thread(target=self.client.timetable.date_week, args=(
            self.date - datetime.timedelta(7),))
        self.prev_thread.start()

    def build_timetable(self, timetable):
        self.ui.Timetable.setRowCount(len(timetable.days))
        self.ui.Timetable.setColumnCount(len(timetable.days[0].lessons))
        self.ui.Timetable.setVerticalHeaderLabels([
            "{}\n{}".format(day.abbr, datetime.datetime
                            .strftime(datetime.datetime
                                      .strptime(day.date, "%Y%m%d"), "%x"))
            for day in timetable.days
        ])
        self.ui.Timetable.setHorizontalHeaderLabels([
            "{}\n{} - {}".format(header.caption, header.time_begin, header.time_end) for header in timetable.headers
        ])

        self.ui.menuWeek.setTitle(timetable.cycle_name.capitalize())

        for i, day in enumerate(timetable.days):
            for x, lesson in enumerate(day.lessons):
                if not lesson.type == "X":
                    item = QtWidgets.QTableWidgetItem("{}\n{}\n{}".format(
                        lesson.abbr, lesson.teacher_abbr, lesson.room_abbr))
                    if lesson.change_description is not None:
                        item.setBackground(QtGui.QColor(255, 0, 0))
                    item.details = lesson
                else:
                    item = QtWidgets.QTableWidgetItem("")
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.Timetable.setItem(i, x, item)

        self.ui.Timetable.resizeColumnsToContents()
        self.ui.Timetable.resizeRowsToContents()

    def cell_click(self, row, col):
        try:
            item = self.ui.Timetable.item(row, col).details
            details = [item.name, item.theme, item.teacher, item.room if item.room else item.room_abbr,
                       item.change_description if item.change_description else None]
            details = [detail for detail in details if detail is not None]
            QtWidgets.QMessageBox.information(
                self, "Detaily", "\n".join(details))
        except AttributeError:
            pass


class ThreadUserInfo(QtCore.QThread):
    send_info = QtCore.Signal(object)

    def __init__(self, client):
        super().__init__()
        self.client = client

    def run(self):
        self.send_info.emit(self.client.info())


class SelectorWindow(QtWidgets.QMainWindow):
    send_client = QtCore.Signal(bakalib.Client)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.ui = Ui_selectorWindow()
        self.ui.setupUi(self)

        if not studentui.paths.auth_file.is_file():
            self.login = LoginDialog()
            self.login.login_send_client.connect(self.run)
            self.login.show()

    def run(self, client):
        self.login.close()

        self.timetable_window = TimetableWindow(client=client)
        #self.grades_window = GradesWindow(client=client)
        #self.absence_window = AbsenceWindow(client=client)

        self.ui.pushTimetable.clicked.connect(self.run_timetable)
        self.ui.pushGrades.clicked.connect(self.run_grades)
        self.ui.pushAbsence.clicked.connect(self.run_absence)
        self.ui.pushLogout.clicked.connect(self.logout)

        self.info_thread = ThreadUserInfo(client)
        self.info_thread.start()
        self.info_thread.send_info.connect(self.update_info)

        self.show()

    def update_info(self, info):
        self.ui.labelName.setText(info.name.rstrip(", {}".format(info.class_)))
        self.ui.labelClass.setText(info.class_)
        self.ui.labelSchool.setText(info.school)

    def logout(self):
        self.login.clear()
        self.login.open()
        self.close()

    def run_timetable(self):
        self.timetable_window.show()

    def run_grades(self):
        QtWidgets.QMessageBox.information(self, "WIP", "Něco tu chybí")

    def run_absence(self):
        QtWidgets.QMessageBox.information(self, "WIP", "Něco tu chybí")


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SelectorWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
