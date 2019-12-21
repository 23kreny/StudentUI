# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentui/ui/login.ui',
# licensing of 'studentui/ui/login.ui' applies.
#
# Created: Wed Dec 18 19:45:52 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(195, 247)
        self.gridLayout = QtWidgets.QGridLayout(loginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cityCombo = QtWidgets.QComboBox(loginDialog)
        self.cityCombo.setObjectName("cityCombo")
        self.verticalLayout.addWidget(self.cityCombo)
        self.schoolCombo = QtWidgets.QComboBox(loginDialog)
        self.schoolCombo.setObjectName("schoolCombo")
        self.verticalLayout.addWidget(self.schoolCombo)
        self.lineUser = QtWidgets.QLineEdit(loginDialog)
        self.lineUser.setObjectName("lineUser")
        self.verticalLayout.addWidget(self.lineUser)
        self.linePass = QtWidgets.QLineEdit(loginDialog)
        self.linePass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePass.setObjectName("linePass")
        self.verticalLayout.addWidget(self.linePass)
        self.showpassBox = QtWidgets.QCheckBox(loginDialog)
        self.showpassBox.setObjectName("showpassBox")
        self.verticalLayout.addWidget(self.showpassBox)
        self.rememberBox = QtWidgets.QCheckBox(loginDialog)
        self.rememberBox.setObjectName("rememberBox")
        self.verticalLayout.addWidget(self.rememberBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushLogin = QtWidgets.QPushButton(loginDialog)
        self.pushLogin.setObjectName("pushLogin")
        self.horizontalLayout.addWidget(self.pushLogin)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(loginDialog)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QtWidgets.QApplication.translate("loginDialog", "Login - StudentUI", None, -1))
        self.lineUser.setPlaceholderText(QtWidgets.QApplication.translate("loginDialog", "Přihlašovací jméno", None, -1))
        self.linePass.setPlaceholderText(QtWidgets.QApplication.translate("loginDialog", "Heslo", None, -1))
        self.showpassBox.setText(QtWidgets.QApplication.translate("loginDialog", "Zobrazit heslo", None, -1))
        self.rememberBox.setText(QtWidgets.QApplication.translate("loginDialog", "Přihlašovat automaticky", None, -1))
        self.pushLogin.setText(QtWidgets.QApplication.translate("loginDialog", "Přihlásit se", None, -1))

