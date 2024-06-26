import RPi.GPIO as GPIO
import time

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
	while True:
		a = input("입력(o/x) : ")
		if a == "o":
			GPIO.output(led, False)
		elif a == "x":
			GPIO.output(led, True)
		else:
			print("정확한 문자입력!")
		
except KeyboardInterrupt:
	GPIO.cleanup()