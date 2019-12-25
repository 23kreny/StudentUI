# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentui/ui/timetable.ui',
# licensing of 'studentui/ui/timetable.ui' applies.
#
# Created: Wed Dec 25 10:55:59 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_timetableWindow(object):
    def setupUi(self, timetableWindow):
        timetableWindow.setObjectName("timetableWindow")
        timetableWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(timetableWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushPrev = QtWidgets.QPushButton(self.centralwidget)
        self.pushPrev.setObjectName("pushPrev")
        self.horizontalLayout.addWidget(self.pushPrev)
        self.pushNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushNext.setObjectName("pushNext")
        self.horizontalLayout.addWidget(self.pushNext)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Timetable = QtWidgets.QTableWidget(self.centralwidget)
        self.Timetable.setObjectName("Timetable")
        self.Timetable.setColumnCount(0)
        self.Timetable.setRowCount(0)
        self.verticalLayout.addWidget(self.Timetable)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        timetableWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(timetableWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuWeek = QtWidgets.QMenu(self.menubar)
        self.menuWeek.setObjectName("menuWeek")
        timetableWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuWeek.menuAction())

        self.retranslateUi(timetableWindow)
        QtCore.QMetaObject.connectSlotsByName(timetableWindow)

    def retranslateUi(self, timetableWindow):
        timetableWindow.setWindowTitle(QtWidgets.QApplication.translate("timetableWindow", "Rozvrh - StudentUI", None, -1))
        self.pushPrev.setText(QtWidgets.QApplication.translate("timetableWindow", "<<", None, -1))
        self.pushNext.setText(QtWidgets.QApplication.translate("timetableWindow", ">>", None, -1))
        self.menuWeek.setTitle(QtWidgets.QApplication.translate("timetableWindow", "*", None, -1))

