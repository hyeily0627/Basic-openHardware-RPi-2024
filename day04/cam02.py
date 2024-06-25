import RPi.GPIO as GPIO
import time

switch = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)

oldSw = 0 
newSw = 0

try:
	while True:
		newSw = GPIO.input(switch)
		if newSw != oldSw:
			oldSw = newSw

			if newSw ==1:
				print("click")

				time.sleep(0.2)

except KeyboardInterrupt:
	pass
