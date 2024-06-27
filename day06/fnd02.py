import RPi.GPIO as GPIO
import time

# 0~9까지 1byte 헥사(hex) 값 
fndDatas = [ 0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]
fndSegs = [4, 5, 6, 12, 13, 16, 17]
fndSels = [20, 21, 22, 23]

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data): # 하나의 숫자 형태를 만드는 함수 
	for i in range(0,7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
		
try:
	while True:
		for i in range(0,2):
			GPIO.output(fndSels[i], 0) 	#fnd 선택

			for j in range(0,10):
				fndOut(j)
				time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup() 
