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

@app.route("/led/<state>")
def control(state):
	if state == "on":
		GPIO.output(led, False)
		return "불 켜져요🚨"
	elif state == "off":
		GPIO.output(led, True)
		return "불 꺼져요🚨"
	elif state == "clear":
		GPIO.cleanup()
		return "GPIO cleanup()"

if __name__ == "__main__":  #터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다 
	app.run(host="0.0.0.0",port=10111, debug=True) #실행을 위한 명령문으로 보면 된다
