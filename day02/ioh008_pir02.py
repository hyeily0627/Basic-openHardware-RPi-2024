# title : ioh008_pir02.py
# date : 2024-06-21
# desc : 동작감지센서 + LED

import RPi.GPIO as GPIO
import time

pirPin = 24
led = 16
count = 1

GPIO.setmode(GPIO.BCM)
# GPIO.setup(pirPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == True:
			print("Detected", count)
			GPIO.output(led, False)
			time.sleep(3)
			GPIO.output(led, True)
			count += 1

except KeyboardInterrupt:
	GPIO.cleanup()
	print("System OFF")
