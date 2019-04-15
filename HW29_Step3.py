# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_box.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
'''user code'''
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
led = LED(23) # for the LED toggling project

ledPin = 24 # for the LED dimmer project
GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 100)
pwm.start(100)

def toggleLED():
    if led.is_lit:
        led.off()
    else:
        led.on()
'''user code'''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 130, 250, 131))
        font = QtGui.QFont()
        font.setFamily("Stencil Std")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        
        '''user code'''
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        '''user code'''
        
        self.verticalSlider.setGeometry(QtCore.QRect(370, 70, 101, 291))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "Toggle LED"))
        '''user code'''
        self.pushButton.clicked.connect(toggleLED)
        self.verticalSlider.valueChanged.connect(self.sliderMove)
        
    def sliderMove(self):
        value = self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
        '''user code'''

'''user code'''
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
'''user code'''
