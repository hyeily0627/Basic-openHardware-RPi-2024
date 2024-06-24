import RPi.GPIO as GPIO
import time 

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for step in steps:
	GPIO.setup(steps, GPIO.OUT) 
	GPIO.output(steps, 0) 

try:
	while 1:
		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 1)
		time.sleep(0.01)

		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 1)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)

		GPIO.output(steps[0], 0)
		GPIO.output(steps[1], 1)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)

		GPIO.output(steps[0], 1)
		GPIO.output(steps[1], 0)
		GPIO.output(steps[2], 0)
		GPIO.output(steps[3], 0)
		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup() 
