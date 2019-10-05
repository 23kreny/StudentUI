# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentui/ui/grades.ui',
# licensing of 'studentui/ui/grades.ui' applies.
#
# Created: Fri Oct  4 22:12:13 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_gradesWindow(object):
    def setupUi(self, gradesWindow):
        gradesWindow.setObjectName("gradesWindow")
        gradesWindow.resize(788, 675)
        self.centralwidget = QtWidgets.QWidget(gradesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeGrades = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeGrades.setObjectName("treeGrades")
        self.horizontalLayout.addWidget(self.treeGrades)
        self.listDetails = QtWidgets.QListWidget(self.centralwidget)
        self.listDetails.setObjectName("listDetails")
        self.horizontalLayout.addWidget(self.listDetails)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        gradesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(gradesWindow)
        self.statusbar.setObjectName("statusbar")
        gradesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(gradesWindow)
        QtCore.QMetaObject.connectSlotsByName(gradesWindow)

    def retranslateUi(self, gradesWindow):
        gradesWindow.setWindowTitle(QtWidgets.QApplication.translate("gradesWindow", "Známky - StudentUI", None, -1))
        self.treeGrades.headerItem().setText(0, QtWidgets.QApplication.translate("gradesWindow", "Známky", None, -1))

