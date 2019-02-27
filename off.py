# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'off.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_off(object):
    def setupUi(self, off):
        off.setObjectName("off")
        off.resize(201, 150)
        off.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color:rgb(85, 170, 255)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(off)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 60, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 90, 60, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        off.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(off)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 201, 26))
        self.menubar.setObjectName("menubar")
        off.setMenuBar(self.menubar)

        self.retranslateUi(off)
        QtCore.QMetaObject.connectSlotsByName(off)

    def retranslateUi(self, off):
        _translate = QtCore.QCoreApplication.translate
        off.setWindowTitle(_translate("off", "MainWindow"))
        self.pushButton.setText(_translate("off", "注销"))
        self.label.setText(_translate("off", "请选择"))
        self.pushButton_2.setText(_translate("off", "退出"))
        self.pushButton_3.setText(_translate("off", "×"))

