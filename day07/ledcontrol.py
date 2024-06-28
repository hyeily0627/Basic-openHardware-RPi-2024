from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import RPi.GPIO as GPIO

form_class = uic.loadUiType("./ledcontrol.ui")[0]

# GPIO 핀 번호 설정
red_pin = 19
green_pin = 13
blue_pin = 6

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # GPIO 설정
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)

        # 이벤트 함수 등록
        self.BtnOn.clicked.connect(self.BtnOnFunction)
        self.BtnRed.clicked.connect(self.BtnRedFunction)
        self.BtnBlue.clicked.connect(self.BtnBlueFunction)
        self.BtnGreen.clicked.connect(self.BtnGreenFunction)

    def BtnOnFunction(self):
        print("불을 켭니다")
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, False)
        
    def BtnRedFunction(self):
        print("빨간색 불이 켜집니다")
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, True)
        
    def BtnBlueFunction(self):
        print("파란색 불이 켜집니다")
        GPIO.output(red_pin, True)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, False)
        
    def BtnGreenFunction(self):
        print("초록색 불이 켜집니다")
        GPIO.output(red_pin, True)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
