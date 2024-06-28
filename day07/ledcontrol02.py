from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import RPi.GPIO as GPIO
import os

# 권한 조정 (스크립트를 실행하는 사용자가 sudo 권한이 있는 경우)
try:
    os.chmod('/run/user/1000', 0o700)
except PermissionError as e:
    print(f"PermissionError: {e}")

class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ledcontrol.ui", self)

        # GPIO 핀 번호 설정
        self.red_pin = 19
        self.green_pin = 13
        self.blue_pin = 6

        # GPIO 설정
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

        # 이벤트 함수 등록
        self.BtnOn.clicked.connect(self.BtnOnFunction)
        self.BtnRed.clicked.connect(self.BtnRedFunction)
        self.BtnBlue.clicked.connect(self.BtnBlueFunction)
        self.BtnGreen.clicked.connect(self.BtnGreenFunction)

    def BtnOnFunction(self):
        print("불을 켭니다")
        GPIO.output(self.red_pin, True)
        GPIO.output(self.green_pin, True)
        GPIO.output(self.blue_pin, True)
        
    def BtnRedFunction(self):
        print("빨간색 불이 켜집니다")
        GPIO.output(self.red_pin, True)
        GPIO.output(self.green_pin, False)
        GPIO.output(self.blue_pin, False)
        
    def BtnBlueFunction(self):
        print("파란색 불이 켜집니다")
        GPIO.output(self.red_pin, False)
        GPIO.output(self.green_pin, False)
        GPIO.output(self.blue_pin, True)
        
    def BtnGreenFunction(self):
        print("초록색 불이 켜집니다")
        GPIO.output(self.red_pin, False)
        GPIO.output(self.green_pin, True)
        GPIO.output(self.blue_pin, False)

    def closeEvent(self, event):
        GPIO.cleanup()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
