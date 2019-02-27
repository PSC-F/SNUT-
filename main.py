import sys
import os
import Cut
import time
import shutil
import base64
import requests
import urllib.parse
import json
import Get_Json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from login import Ui_login
from list import Ui_list
from off import Ui_off
from end import Ui_end
from scspdl import Ui_scspdl

Arr_person_num = []
Arr_person_in = []
Arr_person_out = []


class ScspdlWindows(QtWidgets.QMainWindow, Ui_scspdl):
    def __init__(self):
        super(ScspdlWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.end)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.openimage)
        self.pushButton_4.clicked.connect(self.drsp)
        self.pushButton_5.clicked.connect(self.zstp)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def drsp(self):
        # VIDEO_PATH = 'E:\\VideoSource\\test15.mp4'  # 视频地址
        EXTRACT_FOLDER = 'E:\\CutVedio'  # 存放帧图片的位置
        try:
            shutil.rmtree(EXTRACT_FOLDER)
        except OSError:
            pass
        VIDEO_PATH = QFileDialog.getOpenFileName(self, "导入视频", "", "*.mp4;;All Files(*)")[0]
        self.label_3.setText('导入中...请稍等...')
        QApplication.processEvents()
        print(VIDEO_PATH)
        # EXTRACT_FREQUENCY = 7  # 帧提取频率
        # num = 1  # 图片命名索引序号
        os.mkdir(EXTRACT_FOLDER)  # 判断待分割路径是否存在
        Cut.extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)  # 调用分割函数
        self.label_3.setText('导入成功,等待分析...')

    def openimage(self):
        self.label_3.setText('分析中...请稍等...')
        EXTRACT_FOLDER = 'E:\\ResultImg'  # 存放图片的位置
        try:
            shutil.rmtree(EXTRACT_FOLDER)
        except OSError:
            pass
        os.mkdir(EXTRACT_FOLDER)
        #  Show_F = 'True'  # 默认为真
        num = 1
        Person_num = 100
        Person_in = 0
        Perspm_out = 0
        Count_num = len(os.listdir('E:/CutVedio'))
        while num <= Count_num:
            if num == 1:  # 第一张
                try:
                    area = "10,650,1910,650,1910,1070,10,1070"
                    Num = str(num)
                    path = "E:\\CutVedio\\" + Num + ".jpg"  # 序列图片文件地址
                    if os.path.isfile(path):  # 判断是图片否存在
                        f = open('E:\\CutVedio\\' + Num + '.jpg', 'rb')
                        img = base64.b64encode(f.read())
                        '''area = "10,650,1910,650,1910,1070,10,1070"
                        params = {"dynamic": 'True', "case_id": 0, "case_init": Show_F, "image": img, 'show': 'true',
                                  "area": area}
                        urllib.parse.urlencode(params)
                       # request = requests.post(url=request_url, data=params, headers=header, timeout=None)
                        httpsession = requests.session()
                        request = httpsession.post(url=request_url, data=params, headers=header)'''
                        dic = json.loads(Get_Json.get_body_num(img, area, True, True))  # 获取人流原始返回值转换成dict类型
                        Sava_image = Get_Json.dictget(dic, 'image')  # 第二次调用dictget获取目标数据
                        Sava_personin = Get_Json.dictget(dic, 'in')
                        Sava_personout = Get_Json.dictget(dic, 'out')
                        Save_person_num = Get_Json.dictget(dic, 'person_num')
                        # print(Get_Json.get_body_attr(img, 'gender'))  # 识别人体属性
                        Person_num = Person_num + Sava_personin - Sava_personout
                        Person_in = Person_in + Sava_personin
                        Perspm_out = Perspm_out + Sava_personout
                        Arr_person_num.append(Person_num)
                        Arr_person_in.append(Person_in)
                        Arr_person_out.append(Perspm_out)
                        imagedata = base64.b64decode(Sava_image)  # 解码
                        try:
                            file = open('E:\\ResultImg\\' + Num + '.jpg', "wb")  # 解码后写入Result文件
                            file.write(imagedata)
                            file.close()
                            jpg = QPixmap("E:/ResultImg/" + str(Num) + ".jpg")
                            self.label.setScaledContents(True)
                            self.label.setPixmap(jpg)
                            self.label_2.setText(
                                '当前人数：' + str(Person_num) + '\n进入人数：' + str(Person_in) + '\n离开人数：' + str(
                                    Perspm_out) + '\n' + str(Num))
                            QApplication.processEvents()
                        except Exception as e:
                            print('2' + e)
                        num = num + 1
                        print("渲染中" + Num)
                except Exception as e:
                    print(e)
                    continue
            else:  # 第二张图片
                try:
                    area = "10,650,1910,650,1910,1070,10,1070"
                    Num = str(num)
                    path = "E:\\CutVedio\\" + Num + ".jpg"  # 序列图片文件地址
                    if os.path.isfile(path):  # 判断是图片否存在
                        f = open('E:\\CutVedio\\' + Num + '.jpg', 'rb')
                        img = base64.b64encode(f.read())
                        dic = json.loads(Get_Json.get_body_num(img, area, False, False))  # 获取人流原始返回值转换成dict类型
                        Sava_image = Get_Json.dictget(dic, 'image')  # 第二次调用dictget获取目标数据
                        Sava_personin = Get_Json.dictget(dic, 'in')
                        Sava_personout = Get_Json.dictget(dic, 'out')
                        Save_person_num = Get_Json.dictget(dic, 'person_num')
                        # print(Get_Json.get_body_attr(img, 'gender'))  # 识别人体属性
                        Person_num = Person_num + Sava_personin - Sava_personout
                        Person_in = Person_in + Sava_personin
                        Perspm_out = Perspm_out + Sava_personout
                        Arr_person_num.append(Person_num)
                        Arr_person_in.append(Person_in)
                        Arr_person_out.append(Perspm_out)
                        imagedata = base64.b64decode(Sava_image)  # 解码
                        try:
                            file = open('E:\\ResultImg\\' + Num + '.jpg', "wb")  # 解码后写入Result文件
                            file.write(imagedata)
                            file.close()
                            jpg = QPixmap("E:/ResultImg/" + str(Num) + ".jpg")
                            self.label.setScaledContents(True)
                            self.label.setPixmap(jpg)
                            self.label_2.setText(
                                '当前人数：' + str(Person_num) + '\n进入人数：' + str(Person_in) + '\n离开人数：' + str(
                                    Perspm_out) + '\n' + str(Num))
                            QApplication.processEvents()
                        except Exception as e:
                            print('3' + e)
                        num = num + 1
                        print("渲染中" + Num)
                except Exception as e:
                    print('1' + e)
                    continue
        self.label_3.setText('分析完成,等待展示...')

    def zstp(self):
        self.label_3.setText('展示中...')
        a = len(os.listdir('E:/ResultImg'))
        print(a)
        print(Arr_person_num)
        print(Arr_person_in)
        print(Arr_person_out)
        for i in range(1, a + 1):
            jpg = QPixmap("E:/ResultImg/" + str(i) + ".jpg")
            self.label.setScaledContents(True)
            self.label.setPixmap(jpg)
            self.label_2.setText(
                '当前人数：' + str(Arr_person_num[i - 1]) + '\n进入人数：' + str(Arr_person_in[i - 1]) + '\n离开人数：' + str(
                    Arr_person_out[i - 1]))
            print(i)
            QApplication.processEvents()

    def end(self):
        self.a = EndWindows()
        self.a.show()
        self.a.pushButton.clicked.connect(self.hide)


class EndWindows(QtWidgets.QMainWindow, Ui_end):  # 退出
    def __init__(self):
        super(EndWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.hide)


class OffWindows(QtWidgets.QMainWindow, Ui_off):  # 注销
    def __init__(self):
        super(OffWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.hide)

    def login(self):
        self.hide()
        self.b = ListWindows()
        self.b.hide()
        self.a = LoginWindows()
        self.a.show()


class ListWindows(QtWidgets.QMainWindow, Ui_list):
    def __init__(self):
        super(ListWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.off)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton_4.clicked.connect(self.scspdl)

    def off(self):
        self.a = OffWindows()
        self.a.show()
        self.a.pushButton.clicked.connect(self.hide)

    def scspdl(self):
        self.hide()
        self.a = ScspdlWindows()
        self.a.show()
        # self.a.a.pushButton.clicked.connect(self.show)
        # self.a.pushButton.clicked.connect(self.hide)


class LoginWindows(QtWidgets.QMainWindow, Ui_login):
    def __init__(self):
        super(LoginWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_3.clicked.connect(self.end)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton.clicked.connect(self.login)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def end(self):
        self.a = EndWindows()
        self.a.show()

    def login(self):
        self.hide()
        self.a = ListWindows()
        self.a.show()

        '''if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'admin':
            self.hide()
            self.a = ListWindows()
            self.a.show()
        else:
            self.label_4.setText('用户名或密码输入错误')'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindows()
    login.show()
    # login.lineEdit_2.setEchoMode(QLineEdit.Password)
    # login.pushButton.clicked.connect(sys.exit)
    # login.pushButton_2.clicked.connect(login.showMinimized)
    sys.exit(app.exec_())
'''import sys#无用
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_end()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
import sys
import os
import Cut
import time
import shutil
import base64
import requests
import urllib.parse
import json
import Get_Json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from login import Ui_login
from list import Ui_list
from off import Ui_off
from end import Ui_end
from scspdl import Ui_scspdl

Arr_person_num = []
Arr_person_in = []
Arr_person_out = []


class ScspdlWindows(QtWidgets.QMainWindow, Ui_scspdl):
    def __init__(self):
        super(ScspdlWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.end)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton_3.clicked.connect(self.openimage)
        self.pushButton_4.clicked.connect(self.drsp)
        self.pushButton_5.clicked.connect(self.zstp)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def drsp(self):
        # VIDEO_PATH = 'E:\\VideoSource\\test15.mp4'  # 视频地址
        EXTRACT_FOLDER = 'E:\\CutVedio'  # 存放帧图片的位置
        try:
            shutil.rmtree(EXTRACT_FOLDER)
        except OSError:
            pass
        VIDEO_PATH = QFileDialog.getOpenFileName(self, "导入视频", "", "*.mp4;;All Files(*)")[0]
        self.label_3.setText('导入中...请稍等...')
        QApplication.processEvents()
        print(VIDEO_PATH)
        # EXTRACT_FREQUENCY = 7  # 帧提取频率
        # num = 1  # 图片命名索引序号
        os.mkdir(EXTRACT_FOLDER)  # 判断待分割路径是否存在
        Cut.extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)  # 调用分割函数
        self.label_3.setText('导入成功,等待分析...')

    def openimage(self):
        self.label_3.setText('分析中...请稍等...')
        EXTRACT_FOLDER = 'E:\\ResultImg'  # 存放图片的位置
        try:
            shutil.rmtree(EXTRACT_FOLDER)
        except OSError:
            pass
        os.mkdir(EXTRACT_FOLDER)
        #  Show_F = 'True'  # 默认为真
        num = 1
        Person_num = 100
        Person_in = 0
        Perspm_out = 0
        Count_num = len(os.listdir('E:/CutVedio'))
        while num <= Count_num:
            if num == 1:  # 第一张
                try:
                    area = "10,650,1910,650,1910,1070,10,1070"
                    Num = str(num)
                    path = "E:\\CutVedio\\" + Num + ".jpg"  # 序列图片文件地址
                    if os.path.isfile(path):  # 判断是图片否存在
                        f = open('E:\\CutVedio\\' + Num + '.jpg', 'rb')
                        img = base64.b64encode(f.read())
                        '''area = "10,650,1910,650,1910,1070,10,1070"
                        params = {"dynamic": 'True', "case_id": 0, "case_init": Show_F, "image": img, 'show': 'true',
                                  "area": area}
                        urllib.parse.urlencode(params)
                       # request = requests.post(url=request_url, data=params, headers=header, timeout=None)
                        httpsession = requests.session()
                        request = httpsession.post(url=request_url, data=params, headers=header)'''
                        dic = json.loads(Get_Json.get_body_num(img, area, True, True))  # 获取人流原始返回值转换成dict类型
                        Sava_image = Get_Json.dictget(dic, 'image')  # 第二次调用dictget获取目标数据
                        Sava_personin = Get_Json.dictget(dic, 'in')
                        Sava_personout = Get_Json.dictget(dic, 'out')
                        Save_person_num = Get_Json.dictget(dic, 'person_num')
                        # print(Get_Json.get_body_attr(img, 'gender'))  # 识别人体属性
                        Person_num = Person_num + Sava_personin - Sava_personout
                        Person_in = Person_in + Sava_personin
                        Perspm_out = Perspm_out + Sava_personout
                        Arr_person_num.append(Person_num)
                        Arr_person_in.append(Person_in)
                        Arr_person_out.append(Perspm_out)
                        imagedata = base64.b64decode(Sava_image)  # 解码
                        try:
                            file = open('E:\\ResultImg\\' + Num + '.jpg', "wb")  # 解码后写入Result文件
                            file.write(imagedata)
                            file.close()
                            jpg = QPixmap("E:/ResultImg/" + str(Num) + ".jpg")
                            self.label.setScaledContents(True)
                            self.label.setPixmap(jpg)
                            self.label_2.setText(
                                '当前人数：' + str(Person_num) + '\n进入人数：' + str(Person_in) + '\n离开人数：' + str(
                                    Perspm_out) + '\n' + str(Num))
                            QApplication.processEvents()
                        except Exception as e:
                            print('2' + e)
                        num = num + 1
                        print("渲染中" + Num)
                except Exception as e:
                    print(e)
                    continue
            else:  # 第二张图片
                try:
                    area = "10,650,1910,650,1910,1070,10,1070"
                    Num = str(num)
                    path = "E:\\CutVedio\\" + Num + ".jpg"  # 序列图片文件地址
                    if os.path.isfile(path):  # 判断是图片否存在
                        f = open('E:\\CutVedio\\' + Num + '.jpg', 'rb')
                        img = base64.b64encode(f.read())
                        dic = json.loads(Get_Json.get_body_num(img, area, False, False))  # 获取人流原始返回值转换成dict类型
                        Sava_image = Get_Json.dictget(dic, 'image')  # 第二次调用dictget获取目标数据
                        Sava_personin = Get_Json.dictget(dic, 'in')
                        Sava_personout = Get_Json.dictget(dic, 'out')
                        Save_person_num = Get_Json.dictget(dic, 'person_num')
                        # print(Get_Json.get_body_attr(img, 'gender'))  # 识别人体属性
                        Person_num = Person_num + Sava_personin - Sava_personout
                        Person_in = Person_in + Sava_personin
                        Perspm_out = Perspm_out + Sava_personout
                        Arr_person_num.append(Person_num)
                        Arr_person_in.append(Person_in)
                        Arr_person_out.append(Perspm_out)
                        imagedata = base64.b64decode(Sava_image)  # 解码
                        try:
                            file = open('E:\\ResultImg\\' + Num + '.jpg', "wb")  # 解码后写入Result文件
                            file.write(imagedata)
                            file.close()
                            jpg = QPixmap("E:/ResultImg/" + str(Num) + ".jpg")
                            self.label.setScaledContents(True)
                            self.label.setPixmap(jpg)
                            self.label_2.setText(
                                '当前人数：' + str(Person_num) + '\n进入人数：' + str(Person_in) + '\n离开人数：' + str(
                                    Perspm_out) + '\n' + str(Num))
                            QApplication.processEvents()
                        except Exception as e:
                            print('3' + e)
                        num = num + 1
                        print("渲染中" + Num)
                except Exception as e:
                    print('1' + e)
                    continue
        self.label_3.setText('分析完成,等待展示...')

    def zstp(self):
        self.label_3.setText('展示中...')
        a = len(os.listdir('E:/ResultImg'))
        print(a)
        print(Arr_person_num)
        print(Arr_person_in)
        print(Arr_person_out)
        for i in range(1, a + 1):
            jpg = QPixmap("E:/ResultImg/" + str(i) + ".jpg")
            self.label.setScaledContents(True)
            self.label.setPixmap(jpg)
            self.label_2.setText(
                '当前人数：' + str(Arr_person_num[i - 1]) + '\n进入人数：' + str(Arr_person_in[i - 1]) + '\n离开人数：' + str(
                    Arr_person_out[i - 1]))
            print(i)
            QApplication.processEvents()

    def end(self):
        self.a = EndWindows()
        self.a.show()
        self.a.pushButton.clicked.connect(self.hide)


class EndWindows(QtWidgets.QMainWindow, Ui_end):  # 退出
    def __init__(self):
        super(EndWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.hide)


class OffWindows(QtWidgets.QMainWindow, Ui_off):  # 注销
    def __init__(self):
        super(OffWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(sys.exit)
        self.pushButton_3.clicked.connect(self.hide)

    def login(self):
        self.hide()
        self.b = ListWindows()
        self.b.hide()
        self.a = LoginWindows()
        self.a.show()


class ListWindows(QtWidgets.QMainWindow, Ui_list):
    def __init__(self):
        super(ListWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.pushButton.clicked.connect(self.off)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton_4.clicked.connect(self.scspdl)

    def off(self):
        self.a = OffWindows()
        self.a.show()
        self.a.pushButton.clicked.connect(self.hide)

    def scspdl(self):
        self.hide()
        self.a = ScspdlWindows()
        self.a.show()
        # self.a.a.pushButton.clicked.connect(self.show)
        # self.a.pushButton.clicked.connect(self.hide)


class LoginWindows(QtWidgets.QMainWindow, Ui_login):
    def __init__(self):
        super(LoginWindows, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinMaxButtonsHint)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton_3.clicked.connect(self.end)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.pushButton.clicked.connect(self.login)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def end(self):
        self.a = EndWindows()
        self.a.show()

    def login(self):
        self.hide()
        self.a = ListWindows()
        self.a.show()

        '''if self.lineEdit.text() == 'admin' and self.lineEdit_2.text() == 'admin':
            self.hide()
            self.a = ListWindows()
            self.a.show()
        else:
            self.label_4.setText('用户名或密码输入错误')'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LoginWindows()
    login.show()
    # login.lineEdit_2.setEchoMode(QLineEdit.Password)
    # login.pushButton.clicked.connect(sys.exit)
    # login.pushButton_2.clicked.connect(login.showMinimized)
    sys.exit(app.exec_())
'''import sys#无用
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_end()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
