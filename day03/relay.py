import RPi.GPIO as GPIO
import time 

relayPin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin,GPIO.OUT)

try:
	while True:
		GPIO.output(relayPin,1) # 릴레이 켜기
		time.sleep(1) # 1초 대기
		GPIO.output(relayPin,0) # 릴레이 끄기
		time.sleep(1) # 1초 대기 
		
except KeyboardInterrupt:
	GPIO.cleanup() 
