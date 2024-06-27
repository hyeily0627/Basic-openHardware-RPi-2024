import RPi.GPIO as GPIO
import time

# 0~9까지 1byte 헥사(hex) 값
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]
fndSegs = [4, 5, 6, 12, 13, 16, 17]
fndSels = [20, 21, 22, 23]

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
    GPIO.setup(fndSeg, GPIO.OUT)
    GPIO.output(fndSeg, 0)

for fndSel in fndSels:
    GPIO.setup(fndSel, GPIO.OUT)
    GPIO.output(fndSel, 1)

def fndOut(data, sel): # 하나의 숫자 형태를 만드는 함수
    for i in range(0, 7):
        GPIO.output(fndSegs[i], (fndDatas[data] & (0x01 << i)) != 0)
    for j in range(0, 4): # 표시할 자리수 fnd 만 on
        if j == sel:
            GPIO.output(fndSels[j], 0)
        else:
            GPIO.output(fndSels[j], 1)

count = 0

try:
    while True:
        count += 1
        d1000 = count // 1000 # 천의자리
        d100 = (count % 1000) // 100 # 백의 자리
        d10 = (count % 100) // 10 # 십의 자리
        d1 = count % 10 # 일의 자리
        d = [d1, d10, d100, d1000]

        for i in range(3, -1, -1): # 1 감소시키면서 진행
            fndOut(d[i], i) # 자리수와 값을 전달
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
