# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1661, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.open_buttom.setGeometry(QtCore.QRect(10, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.open_buttom.setFont(font)
        self.open_buttom.setObjectName("open_buttom")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(10, 70, 256, 256))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.img.setFont(font)
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.fft_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.fft_buttom.setGeometry(QtCore.QRect(350, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fft_buttom.setFont(font)
        self.fft_buttom.setObjectName("fft_buttom")
        self.fft_img = QtWidgets.QLabel(self.centralwidget)
        self.fft_img.setGeometry(QtCore.QRect(560, 70, 256, 256))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fft_img.setFont(font)
        self.fft_img.setAlignment(QtCore.Qt.AlignCenter)
        self.fft_img.setObjectName("fft_img")
        self.ifft_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.ifft_buttom.setGeometry(QtCore.QRect(880, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ifft_buttom.setFont(font)
        self.ifft_buttom.setObjectName("ifft_buttom")
        self.ifft_img = QtWidgets.QLabel(self.centralwidget)
        self.ifft_img.setGeometry(QtCore.QRect(1090, 70, 256, 256))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ifft_img.setFont(font)
        self.ifft_img.setAlignment(QtCore.Qt.AlignCenter)
        self.ifft_img.setObjectName("ifft_img")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(1390, 40, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(1430, 160, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.open_buttom_2 = QtWidgets.QPushButton(self.centralwidget)
        self.open_buttom_2.setGeometry(QtCore.QRect(10, 380, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.open_buttom_2.setFont(font)
        self.open_buttom_2.setObjectName("open_buttom_2")
        self.ori_img = QtWidgets.QLabel(self.centralwidget)
        self.ori_img.setGeometry(QtCore.QRect(10, 430, 256, 256))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ori_img.setFont(font)
        self.ori_img.setAlignment(QtCore.Qt.AlignCenter)
        self.ori_img.setObjectName("ori_img")
        self.resized_img = QtWidgets.QLabel(self.centralwidget)
        self.resized_img.setGeometry(QtCore.QRect(350, 320, 480, 480))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.resized_img.setFont(font)
        self.resized_img.setAlignment(QtCore.Qt.AlignCenter)
        self.resized_img.setObjectName("resized_img")
        self.Bilinear_img = QtWidgets.QLabel(self.centralwidget)
        self.Bilinear_img.setGeometry(QtCore.QRect(920, 320, 480, 480))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Bilinear_img.setFont(font)
        self.Bilinear_img.setAlignment(QtCore.Qt.AlignCenter)
        self.Bilinear_img.setObjectName("Bilinear_img")
        self.time_2 = QtWidgets.QLabel(self.centralwidget)
        self.time_2.setGeometry(QtCore.QRect(1440, 520, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.time_2.setFont(font)
        self.time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_2.setObjectName("time_2")
        self.text_2 = QtWidgets.QLabel(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(1400, 410, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text_2.setFont(font)
        self.text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_2.setObjectName("text_2")
        self.size_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.size_buttom.setGeometry(QtCore.QRect(140, 380, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.size_buttom.setFont(font)
        self.size_buttom.setObjectName("size_buttom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_buttom.setText(_translate("MainWindow", "Open File"))
        self.img.setText(_translate("MainWindow", "img"))
        self.fft_buttom.setText(_translate("MainWindow", "fft"))
        self.fft_img.setText(_translate("MainWindow", "fft_img"))
        self.ifft_buttom.setText(_translate("MainWindow", "ifft"))
        self.ifft_img.setText(_translate("MainWindow", "ifft_img"))
        self.text.setText(_translate("MainWindow", "Spend time"))
        self.time.setText(_translate("MainWindow", "Time"))
        self.open_buttom_2.setText(_translate("MainWindow", "Open File"))
        self.ori_img.setText(_translate("MainWindow", "img"))
        self.resized_img.setText(_translate("MainWindow", "Resized_img"))
        self.Bilinear_img.setText(_translate("MainWindow", "Bilinear_Interpolation"))
        self.time_2.setText(_translate("MainWindow", "Time"))
        self.text_2.setText(_translate("MainWindow", "Spend time"))
        self.size_buttom.setText(_translate("MainWindow", "Resize"))
