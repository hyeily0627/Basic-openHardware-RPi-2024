# title : ioh003_input01.py
# date : 2024-06-20
# desc : 스위치 버튼 활용

import RPi.GPIO as GPIO
import time

switch = 6
red = 16
blue = 20
green = 21
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
	while True:
		if GPIO.input(switch) == True:
			count += 1
			if count%3 == 1:
				print(f"count:{count} -> red")
			if count%3 == 2:
				print(f"count:{count} -> blue")
			if count%3 == 0:
				print(f"count:{count} -> green")
			time.sleep(0.3)

		# red
		if count%3 == 1:
			GPIO.output(red, False)
			GPIO.output(blue, True)
			GPIO.output(green, True)

		# blue
		elif count%3 == 2:
			GPIO.output(red, True)
			GPIO.output(blue, False)
			GPIO.output(green, True)

		# green
		elif count%3 == 0:
			GPIO.output(red, True)
			GPIO.output(blue, True)
			GPIO.output(green, False)

except KeyboardInterrupt:
	GPIO.cleanup()
