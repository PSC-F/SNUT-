# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1500, 817)
        login.setStyleSheet("QMainWindow\n"
"{\n"
"    background-image:url(:/project/背景.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(720, 372, 200, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    background:transparent;\n"
"    border:1px solid rgb(166, 232, 255);\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 365, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 407, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(720, 414, 200, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit\n"
"{\n"
"    background:transparent;\n"
"    border:1px solid rgb(166, 232, 255);\n"
"    border-radius:10px;\n"
"    selection-background-color: rgb(166, 232, 255);\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 460, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color:rgb(166, 232, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background:transparent;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(435, 245, 650, 60))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1470, 9, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1440, 8, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color:rgb(166, 232, 255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 465, 121, 21))
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 26))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.label.setText(_translate("login", "用户名"))
        self.label_2.setText(_translate("login", "密码"))
        self.pushButton.setText(_translate("login", "登录"))
        self.label_3.setText(_translate("login", "基于人工智能的视频导流系统"))
        self.pushButton_3.setText(_translate("login", "×"))
        self.pushButton_2.setText(_translate("login", "-"))

import image_rc
