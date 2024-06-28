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

      self.btnOn.clicked.connect(self.btnOnFunction)
      self.btnOff.clicked.connect(self.btnOffFunction)

      self.btnRed.clicked.connect(self.btnRedFunction)
      self.btnBlue.clicked.connect(self.btnBlueFunction)
      self.btnGreen.clicked.connect(self.btnGreenFunction)
      self.btnWhite.clicked.connect(self.btnWhiteFunction)

      GPIO.setmode(GPIO.BCM)
      GPIO.setup(LED_RED, GPIO.OUT)
      GPIO.setup(LED_BLUE, GPIO.OUT)
      GPIO.setup(LED_GREEN, GPIO.OUT)


   def btnOnFunction(self) :
      print("LED ON CLICK!!")

   def btnOffFunction(self) :
      GPIO.output(LED_RED, True)
      GPIO.output(LED_BLUE, True)
      GPIO.output(LED_GREEN, True)
      GPIO.cleanup()
      print("LED OFF CLICK!!")

   def btnRedFunction(self) :
      GPIO.output(LED_RED, False)
      GPIO.output(LED_BLUE, True)
      GPIO.output(LED_GREEN, True)
      print("LED OFF CLICK!!")

   def btnBlueFunction(self) :
      GPIO.output(LED_RED, True)
      GPIO.output(LED_BLUE, False)
      GPIO.output(LED_GREEN, True)
      print("LED OFF CLICK!!")

   def btnGreenFunction(self) :
      GPIO.output(LED_RED, True)
      GPIO.output(LED_BLUE, True)
      GPIO.output(LED_GREEN, False)
      print("LED OFF CLICK!!")

   def btnWhiteFunction(self) :
      GPIO.output(LED_RED, False)
      GPIO.output(LED_BLUE, False)
      GPIO.output(LED_GREEN, False)
      print("LED OFF CLICK!!")

if __name__ == "__main__" :
   app = QApplication(sys.argv)
   myWindow = WindowClass()
   myWindow.show()
   app.exec_()
