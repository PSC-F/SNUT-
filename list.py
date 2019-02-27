# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_list(object):
    def setupUi(self, list):
        list.setObjectName("list")
        list.resize(1500, 817)
        font = QtGui.QFont()
        font.setPointSize(8)
        list.setFont(font)
        list.setStyleSheet("QMainWindow\n"
"{\n"
"    background-image:url(:/project/400079119.jpg)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(list)
        self.centralwidget.setObjectName("centralwidget")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 80, 500, 90))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 270, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"    background:transparent;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(610, 350, 311, 60))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"    background:transparent;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1158, 670, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"    color:rgb(166, 232, 255);\n"
"    background:transparent;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1470, 9, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    color:rgb(166, 232, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        list.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(list)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 26))
        self.menubar.setObjectName("menubar")
        list.setMenuBar(self.menubar)

        self.retranslateUi(list)
        QtCore.QMetaObject.connectSlotsByName(list)

    def retranslateUi(self, list):
        _translate = QtCore.QCoreApplication.translate
        list.setWindowTitle(_translate("list", "MainWindow"))
        self.pushButton_2.setText(_translate("list", "-"))
        self.label.setText(_translate("list", "请选择您所需要的功能"))
        self.pushButton_3.setText(_translate("list", "电梯识别系统"))
        self.pushButton_4.setText(_translate("list", "人流数据分析系统"))
        self.pushButton_5.setText(_translate("list", "人脸识别系统"))
        self.pushButton.setText(_translate("list", "×"))

import image_rc
