# 현지 코드! 

import RPi.GPIO as GPIO
import time

led = [13, 26, 19, 20, 21, 22, 12]
GPIO.setmode(GPIO.BCM)

for ledPin in led:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, True)

num = [[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

try:
	while True:
		for num_seq in num:
			for pin in range(7):
				GPIO.output(led[pin], num_seq[pin])
			time.sleep(1)
		
except KeyboardInterrupt:
	GPIO.cleanup()
