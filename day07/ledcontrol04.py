import RPi.GPIO as GPIO
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test01.ui")[0]

LED_RED = 19
LED_BLUE = 13
LED_GREEN = 6


class WindowClass(QMainWindow, form_class) :
   def __init__(self) :
      super().__init__()
      self.setupUi(self)

      
      self.Btn_ON.clicked.connect(self.btnOnFunction)
      self.Btn_OFF.clicked.connect(self.btnOffFunction)

      self.Btn_RED.clicked.connect(self.btnRedFunction)
      self.Btn_BLUE.clicked.connect(self.btnBlueFunction)
      self.Btn_GREEN.clicked.connect(self.btnGreenFunction)
      self.Btn_WHITE.clicked.connect(self.btnWhiteFunction)

      
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(LED_RED, GPIO.OUT)
      GPIO.setup(LED_BLUE, GPIO.OUT)
      GPIO.setup(LED_GREEN, GPIO.OUT)

   
   def btnOnFunction(self) :
      print("LED가 활성화 되었습니다")

   def btnOffFunction(self) :
      GPIO.output(LED_RED, True)
      GPIO.output(LED_BLUE, True)
      GPIO.output(LED_GREEN, True)
      GPIO.cleanup()
      print("LED가 종료되었습니다")

   def btnRedFunction(self) :
      GPIO.output(LED_RED, False)
      GPIO.output(LED_BLUE, True)
      GPIO.output(LED_GREEN, True)
      print("빨간불이 켜졌습니다")

   def btnBlueFunction(self) :
      GPIO.output(LED_RED, True)
      GPIO.output(LED_BLUE, False)
      GPIO.output(LED_GREEN, True)
      print("파란불이 켜졌습니다")

   def btnGreenFunction(self) :
      GPIO.output(LED_RED, True)
      GPIO.output(LED_BLUE, True)
      GPIO.output(LED_GREEN, False)
      print("초록불이 켜졌습니다")

   def btnWhiteFunction(self) :
      GPIO.output(LED_RED, False)
      GPIO.output(LED_BLUE, False)
      GPIO.output(LED_GREEN, False)
      print("흰색불이 켜졌습니다")


if __name__ == "__main__" :
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   app.exec_()
