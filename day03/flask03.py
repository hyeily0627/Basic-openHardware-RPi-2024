# URL 접속을 /led/on, /led/off 로 접속하면 
# led를 on, off 할 수 있는 웹페이지를 만들어용

from flask import Flask  #name이름을 통한 flask객체 생성 

import RPi.GPIO as GPIO
import time

app = Flask(__name__)

led = 21

@app.route("/home")
def home():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led, GPIO.OUT)
	GPIO.output(led, True) #꺼진상태
	return "LED를 컨트롤 해봅시다❗"

@app.route("/on")
def led_on():
	GPIO.output(led, False)
	return "불 켜져요🚨"

@app.route("/off")
def led_off():
	GPIO.output(led, True)
	return "불 꺼졌어요"

if __name__ == "__main__":  #터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다 
	app.run(host="0.0.0.0",port=10111, debug=True) #실행을 위한 명령문으로 보면 된다
