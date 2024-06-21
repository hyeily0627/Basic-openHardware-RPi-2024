# title : ioh006_input02.py
# date : 2024-06-20
# desc : 키보드로 값 입력받아 실행시키기

import RPi.GPIO as GPIO
import time

red = 16
blue = 20
green = 21
piezoPin = 13
melody = [130, 147, 165, 175, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)



try:
	GPIO.output(red, True)
	GPIO.output(blue, True)
	GPIO.output(green, True)

	while True:
		a = input()

		# LED ON
		if a == 'r':
			GPIO.output(red, False)
			GPIO.output(blue, True)
			GPIO.output(green, True)
			print("Red LED ON")

		elif a == 'b':
			GPIO.output(red, True)
			GPIO.output(blue, False)
			GPIO.output(green, True)
			print("Blue LED ON")

		elif a == 'g':
			GPIO.output(red, True)
			GPIO.output(blue, True)
			GPIO.output(green, False)
			print("Green LED ON")

		# LED OFF
		elif a == 'X' or a == 'x':
			GPIO.output(led, True)
			print("led OFF!")

		# 부저 소리 켜기
		elif a in ['1','2','3','4','5','6','7','8']:
			b = int(a)
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[b-1])

		# 부저 소리 끄기
		elif a == 'q':
			Buzz.stop()
			print("Buzz OFF!")

except KeyboardInterrupt:
	print("System Off!")
	GPIO.cleanup()
