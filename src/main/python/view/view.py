# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/language.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(828, 520)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.provideLabel = QtWidgets.QLabel(self.centralwidget)
        self.provideLabel.setObjectName("provideLabel")
        self.gridLayout.addWidget(self.provideLabel, 0, 0, 1, 1)
        self.provideEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.provideEdit.setObjectName("provideEdit")
        self.gridLayout.addWidget(self.provideEdit, 1, 0, 1, 3)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setObjectName("resultLabel")
        self.gridLayout.addWidget(self.resultLabel, 2, 0, 1, 1)
        self.resultBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.resultBrowser.setObjectName("resultBrowser")
        self.gridLayout.addWidget(self.resultBrowser, 3, 0, 1, 3)
        self.checkButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkButton.setObjectName("checkButton")
        self.gridLayout.addWidget(self.checkButton, 4, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 4, 1, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 4, 2, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "My Language Tool"))
        self.provideLabel.setText(_translate("mainWindow", "Please provide your text here:"))
        self.resultLabel.setText(_translate("mainWindow", "Here is your result:"))
        self.checkButton.setText(_translate("mainWindow", "Check"))
        self.resetButton.setText(_translate("mainWindow", "Reset"))
        self.closeButton.setText(_translate("mainWindow", "Close"))

