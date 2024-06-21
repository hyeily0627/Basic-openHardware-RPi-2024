# title : iot004_inter01.py
# date : 2024-06-20
# desc : interrupt

import RPi.GPIO as GPIO
import time

# 핀 설정
red_led = 16
blue_led = 20
green_led = 21
switch = 6

# 인터럽트 변수
intFlag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

def ledBlink(channel):
	global intFlag
	if intFlag == False:
		GPIO.output(red_led, True)
		intFlag == True
	else:
		GPIO.output(red_led, False)
		intFlag == False

# Interrupt 설정(switch 핀에 rising 신호가 잡히면 callback 함수를 실행)
GPIO.add_event_detect(switch, GPIO.RISING, callback = ledBlink)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
