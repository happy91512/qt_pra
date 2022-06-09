from fileinput import filename
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from UI import Ui_MainWindow 
from matplotlib import pyplot as plt
import cv2
import os
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.open_buttom.clicked.connect(self.openbuttomClicked)
        self.ui.fft_buttom.clicked.connect(self.fftbuttomClicked)
        self.ui.ifft_buttom.clicked.connect(self.ifftbuttomClicked)
        self.ui.open_buttom_2.clicked.connect(self.openbuttom2Clicked)
         self.ui.size_buttom.clicked.connect(self.sizebuttomClicked)


    def openbuttomClicked(self):
        global filename, filetype
        filename,filetype = QFileDialog.getOpenFileName(self,"./")
        self.ui.fft_img.setText(" ")
        self.ui.ifft_img.setText(" ")    
        show_img = cv2.imread(filename)
        try:
            show_img = cv2.resize(show_img, (256,256), interpolation=cv2.INTER_AREA)
            height, width, channel = show_img.shape
            bytesPerline = 3 * width
            self.qimg = QImage(show_img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.img.setPixmap(QPixmap.fromImage(self.qimg))
        except:
            self.ui.img.setText("This file is not a image!")

    
    def fftbuttomClicked(self):
        try:
            img_arr = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            dft_arr = cv2.dft(np.float32(img_arr) , flags = cv2.DFT_COMPLEX_OUTPUT)
            global dft_shift
            dft_shift = np.fft.fftshift(dft_arr)    
            spectrum = 15*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))
            fftimg = cv2.resize(spectrum, (256,256), interpolation=cv2.INTER_AREA)
            cv2.imwrite("/home/tdd/fft123ybygsa.png", fftimg)
            fftimg = cv2.imread("/home/tdd/fft123ybygsa.png", cv2.IMREAD_GRAYSCALE)
            os.remove("/home/tdd/fft123ybygsa.png")
            self.qimg = QImage(fftimg, 256, 256, 256, QImage.Format_Grayscale8)
            self.ui.fft_img.setPixmap(QPixmap.fromImage(self.qimg))   
        except:
            self.ui.fft_img.setText("This file can't be fft!")

    def ifftbuttomClicked(self):
        try:
            arr_ishift = np.fft.ifftshift(dft_shift)
            idft_arr = cv2.idft(arr_ishift)
            idftimg = cv2.magnitude(idft_arr[:,:,0],idft_arr[:,:,1])
            plt.imsave("/home/tdd/ifft123ybdcygsa.png", idftimg)
            ifftimg = cv2.imread("/home/tdd/ifft123ybdcygsa.png", cv2.IMREAD_GRAYSCALE)
            os.remove("/home/tdd/ifft123ybdcygsa.png")
            ifftimg = cv2.resize(ifftimg, (256,256), interpolation=cv2.INTER_AREA)
            self.qimg = QImage(ifftimg, 256, 256, 256, QImage.Format_Grayscale8)
            self.ui.ifft_img.setPixmap(QPixmap.fromImage(self.qimg)) 
        except:
            self.ui.ifft_img.setText("This file can't be ifft!")
    
    def openbuttom2Clicked(self):
        global filename2, filetype2
        filename2,filetype2 = QFileDialog.getOpenFileName(self,"./")
        self.ui.resized_img.setText(" ")
        self.ui.Bilinear_img.setText(" ")    
        show_img = cv2.imread(filename2)
        try:
            show_img = cv2.resize(show_img, (256,256), interpolation=cv2.INTER_AREA)
            height, width, channel = show_img.shape
            bytesPerline = 3 * width
            self.qimg = QImage(show_img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
            self.ui.ori_img.setPixmap(QPixmap.fromImage(self.qimg))
        except:
            self.ui.ori_img.setText("This file is not a image!")
"""
    def  sizebuttomClicked(self):
        try:
        
        except:"""
