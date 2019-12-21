# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentui/ui/grades.ui',
# licensing of 'studentui/ui/grades.ui' applies.
#
# Created: Wed Dec 18 19:45:52 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_gradesWindow(object):
    def setupUi(self, gradesWindow):
        gradesWindow.setObjectName("gradesWindow")
        gradesWindow.resize(788, 675)
        self.centralwidget = QtWidgets.QWidget(gradesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioSubj = QtWidgets.QRadioButton(self.centralwidget)
        self.radioSubj.setChecked(True)
        self.radioSubj.setObjectName("radioSubj")
        self.horizontalLayout_2.addWidget(self.radioSubj)
        self.radioDate = QtWidgets.QRadioButton(self.centralwidget)
        self.radioDate.setObjectName("radioDate")
        self.horizontalLayout_2.addWidget(self.radioDate)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeGrades = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeGrades.setObjectName("treeGrades")
        self.horizontalLayout.addWidget(self.treeGrades)
        self.listDetails = QtWidgets.QListWidget(self.centralwidget)
        self.listDetails.setObjectName("listDetails")
        self.horizontalLayout.addWidget(self.listDetails)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        gradesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(gradesWindow)
        self.statusbar.setObjectName("statusbar")
        gradesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(gradesWindow)
        QtCore.QMetaObject.connectSlotsByName(gradesWindow)

    def retranslateUi(self, gradesWindow):
        gradesWindow.setWindowTitle(QtWidgets.QApplication.translate("gradesWindow", "Známky - StudentUI", None, -1))
        self.radioSubj.setText(QtWidgets.QApplication.translate("gradesWindow", "Dle předmětu", None, -1))
        self.radioDate.setText(QtWidgets.QApplication.translate("gradesWindow", "Dle data", None, -1))
        self.treeGrades.headerItem().setText(0, QtWidgets.QApplication.translate("gradesWindow", "Známky", None, -1))

