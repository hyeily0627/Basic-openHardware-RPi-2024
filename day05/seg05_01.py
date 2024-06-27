# 1부터 9999까지 카운트하기
import RPi.GPIO as GPIO
import time

segPins = [20,21,12,23,24,25,26]
COM = [4, 5, 6, 13]
GPIO.setmode(GPIO.BCM)

for pin in segPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

for com in COM:
	GPIO.setup(com, GPIO.OUT)

seqs = [
 [0,0,0,0,0,0,1],  # 0
 [1,0,0,1,1,1,1], # 1
 [0,0,1,0,0,1,0], # 2
 [0,0,0,0,1,1,0], # 3
 [1,0,0,1,1,0,0], # 4
 [0,1,0,0,1,0,0], # 5
 [0,1,0,0,0,0,0], # 6
 [0,0,0,1,1,1,1], # 7
 [0,0,0,0,0,0,0], # 8
 [0,0,0,0,1,0,0]  # 9
]

try:
		i= -1
		while True:
		i++
			for num in range(0, 4):
				for reset in COM:
					GPIO.output(reset, False) ## COM이 바뀔 때 마다 초기화
				GPIO.output(COM[num], True) ## COM에 신호인가
				for i in range(0, 7): 
					GPIO.output(segPins[i], seqs[numList[num]][i]) ## 해당하는 숫자 표기
				time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()