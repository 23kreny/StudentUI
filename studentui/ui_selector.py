# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentui/ui/selector.ui',
# licensing of 'studentui/ui/selector.ui' applies.
#
# Created: Wed Dec 18 19:45:52 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_selectorWindow(object):
    def setupUi(self, selectorWindow):
        selectorWindow.setObjectName("selectorWindow")
        selectorWindow.resize(299, 247)
        self.centralwidget = QtWidgets.QWidget(selectorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.labelClass = QtWidgets.QLabel(self.centralwidget)
        self.labelClass.setText("")
        self.labelClass.setObjectName("labelClass")
        self.verticalLayout.addWidget(self.labelClass)
        self.labelSchool = QtWidgets.QLabel(self.centralwidget)
        self.labelSchool.setText("")
        self.labelSchool.setObjectName("labelSchool")
        self.verticalLayout.addWidget(self.labelSchool)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushTimetable = QtWidgets.QPushButton(self.centralwidget)
        self.pushTimetable.setObjectName("pushTimetable")
        self.gridLayout.addWidget(self.pushTimetable, 0, 0, 1, 1)
        self.pushGrades = QtWidgets.QPushButton(self.centralwidget)
        self.pushGrades.setObjectName("pushGrades")
        self.gridLayout.addWidget(self.pushGrades, 0, 1, 1, 1)
        self.pushAbsence = QtWidgets.QPushButton(self.centralwidget)
        self.pushAbsence.setObjectName("pushAbsence")
        self.gridLayout.addWidget(self.pushAbsence, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushLogout = QtWidgets.QPushButton(self.centralwidget)
        self.pushLogout.setObjectName("pushLogout")
        self.verticalLayout_2.addWidget(self.pushLogout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        selectorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectorWindow)
        QtCore.QMetaObject.connectSlotsByName(selectorWindow)

    def retranslateUi(self, selectorWindow):
        selectorWindow.setWindowTitle(QtWidgets.QApplication.translate("selectorWindow", "StudentUI", None, -1))
        self.pushTimetable.setText(QtWidgets.QApplication.translate("selectorWindow", "Rozvrh", None, -1))
        self.pushGrades.setText(QtWidgets.QApplication.translate("selectorWindow", "Známky", None, -1))
        self.pushAbsence.setText(QtWidgets.QApplication.translate("selectorWindow", "Absence", None, -1))
        self.pushLogout.setText(QtWidgets.QApplication.translate("selectorWindow", "Odhlásit se", None, -1))

