import RPi.GPIO as GPIO
import time

switch = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)

try:
	while True:
		if GPIO.input(switch) == True: #풀다운
			print("Pushed")
			time.sleep(0.3)
			
except KeyboardInterrupt:
	GPIO.cleanup()
