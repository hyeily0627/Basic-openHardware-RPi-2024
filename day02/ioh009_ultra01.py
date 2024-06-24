# title : ioh009_ultra01.py
# date : 20224-06-21
# desc : 초음파센서

import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True)	# 10us 동안 high레벨로 trig 출력하여 초음파 발생 준비
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start =time.time()			# 현재시간 저장

	while GPIO.input(echoPin) == False:	# echo가 없을 경우
		start = time.time()				# 현재 시간을 start 변수에 저장
	while GPIO.input(echoPin) == True:	# echo가 있을 경우
		stop = time.time()				# 현재 시간을 stop 변수에 저장
	elapsed = stop  - start				# 걸린 시간 구하고
	distance = (elapsed * 19000) / 2	# 걸린 시간과 초음파 속도를 이용하여 거리 계산

	return distance

#핀 설정

trigPin = 17
echoPin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
	while True:
		distance = measure()
		print("Distance: %.2f cm" %distance)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
