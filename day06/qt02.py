from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

form_class = uic.loadUiType("./test01.ui")[0]

class WindowClass(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# 이벤트 함수등록 
		self.BtnOn.clicked.connect(self.BtnOnFunction)
		self.BtnOff.clicked.connect(self.BtnOffFunction)

	def BtnOnFunction(self):
		print("ON Button clicked")
	def BtnOffFunction(self):
		print("OFF Button clicked")

		# 디자이너에서 이벤트를 넣었을 경우
	def BtnExit(self):
			print("EXIT")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
