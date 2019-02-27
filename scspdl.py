# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scspdl.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_scspdl(object):
    def setupUi(self, scspdl):
        scspdl.setObjectName("scspdl")
        scspdl.resize(1500, 817)
        scspdl.setStyleSheet("QMainWindow\n"
"{\n"
"    background-image:url(:/project/500528250.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(scspdl)
        self.centralwidget.setObjectName("centralwidget")
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 80, 841, 681))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 20, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    border:1px solid rgb(166, 232, 255);\n"
"    border-radius:10px;\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 20, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    border:1px solid rgb(166, 232, 255);\n"
"    border-radius:10px;\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 76, 321, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 20, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"    background:transparent;\n"
"    border:1px solid rgb(166, 232, 255);\n"
"    border-radius:10px;\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 23, 380, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    color:rgb(166, 232, 255)\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        scspdl.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(scspdl)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 26))
        self.menubar.setObjectName("menubar")
        scspdl.setMenuBar(self.menubar)

        self.retranslateUi(scspdl)
        QtCore.QMetaObject.connectSlotsByName(scspdl)

    def retranslateUi(self, scspdl):
        _translate = QtCore.QCoreApplication.translate
        scspdl.setWindowTitle(_translate("scspdl", "MainWindow"))
        self.pushButton.setText(_translate("scspdl", "×"))
        self.pushButton_2.setText(_translate("scspdl", "-"))
        self.pushButton_3.setText(_translate("scspdl", "分析"))
        self.pushButton_4.setText(_translate("scspdl", "导入"))
        self.pushButton_5.setText(_translate("scspdl", "展示"))

import image_rc
