# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentui/ui/selector.ui',
# licensing of 'studentui/ui/selector.ui' applies.
#
# Created: Wed Dec 25 10:55:59 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_selectorWindow(object):
    def setupUi(self, selectorWindow):
        selectorWindow.setObjectName("selectorWindow")
        selectorWindow.resize(308, 281)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(selectorWindow.sizePolicy().hasHeightForWidth())
        selectorWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(selectorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNameClass = QtWidgets.QLabel(self.centralwidget)
        self.labelNameClass.setText("")
        self.labelNameClass.setObjectName("labelNameClass")
        self.verticalLayout.addWidget(self.labelNameClass)
        self.labelSchool = QtWidgets.QLabel(self.centralwidget)
        self.labelSchool.setText("")
        self.labelSchool.setObjectName("labelSchool")
        self.verticalLayout.addWidget(self.labelSchool)
        self.verticalLayout_4.addLayout(self.verticalLayout)
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
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushLogout = QtWidgets.QPushButton(self.centralwidget)
        self.pushLogout.setObjectName("pushLogout")
        self.verticalLayout_3.addWidget(self.pushLogout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.labelSUIVersion = QtWidgets.QLabel(self.centralwidget)
        self.labelSUIVersion.setText("")
        self.labelSUIVersion.setObjectName("labelSUIVersion")
        self.horizontalLayout.addWidget(self.labelSUIVersion)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.labelBakalibVersion = QtWidgets.QLabel(self.centralwidget)
        self.labelBakalibVersion.setText("")
        self.labelBakalibVersion.setObjectName("labelBakalibVersion")
        self.horizontalLayout_2.addWidget(self.labelBakalibVersion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        selectorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(selectorWindow)
        QtCore.QMetaObject.connectSlotsByName(selectorWindow)

    def retranslateUi(self, selectorWindow):
        selectorWindow.setWindowTitle(QtWidgets.QApplication.translate("selectorWindow", "StudentUI", None, -1))
        self.pushTimetable.setText(QtWidgets.QApplication.translate("selectorWindow", "Rozvrh", None, -1))
        self.pushGrades.setText(QtWidgets.QApplication.translate("selectorWindow", "Známky", None, -1))
        self.pushAbsence.setText(QtWidgets.QApplication.translate("selectorWindow", "Absence", None, -1))
        self.pushLogout.setText(QtWidgets.QApplication.translate("selectorWindow", "Odhlásit se", None, -1))

