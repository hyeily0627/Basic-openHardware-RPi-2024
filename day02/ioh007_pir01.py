# title : ioh007_pir01.py
# date : 2024-06-21
# desc : 동작감지센서

import RPi.GPIO as GPIO
import time

pirPin = 24
count = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)

try:
	while True:
		if GPIO.input(pirPin) == True:
			print("Detected", count)
			time.sleep(0.5)
			count += 1

except KeyboardInterrupt:
	GPIO.cleanup()
