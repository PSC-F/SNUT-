# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'end.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_end(object):
    def setupUi(self, end):
        end.setObjectName("end")
        end.resize(200, 150)
        end.setStyleSheet("QMainWindow\n"
"{\n"
"    background-coloc:rgb(0, 170, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(end)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 60, 30))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(85, 85, 255)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 90, 60, 30))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(85, 85, 255)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        end.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(end)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 26))
        self.menubar.setObjectName("menubar")
        end.setMenuBar(self.menubar)

        self.retranslateUi(end)
        QtCore.QMetaObject.connectSlotsByName(end)

    def retranslateUi(self, end):
        _translate = QtCore.QCoreApplication.translate
        end.setWindowTitle(_translate("end", "MainWindow"))
        self.pushButton.setText(_translate("end", "返回"))
        self.pushButton_2.setText(_translate("end", "退出"))
        self.label.setText(_translate("end", "请选择"))
        self.pushButton_3.setText(_translate("end", "×"))

