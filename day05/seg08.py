# 입력한 숫자 띄우기
import RPi.GPIO as GPIO
import time

segPins = [4, 5, 6, 12, 13, 16, 17]
COM = [20, 21, 22, 23]
GPIO.setmode(GPIO.BCM)

for pin in segPins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, True)

for com in COM:
   GPIO.setup(com, GPIO.OUT)

seqs = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [0, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 0, 0, 1, 1]   # 9
]


try:
      NUMBER = input("숫자를 입력하세요(0~9999) >> ")
      List = []
      for i in str(NUMBER): ## 자릿수별 숫자 배열 담기
         List.append(i)
      numList = list(map(int, List)) ## 형변환
      len = len(str(NUMBER)) ## 숫자길이
      size = 4-len ## 좌측 정렬을 위한 변수 size

      while True:
         for num in range(0, len):
            for reset in COM:
               GPIO.output(reset,  False) ## COM이 바뀔 때 마다 초기화
            GPIO.output(COM[num+size], True) ## COM에 신호인가
            for i in range(0, 7): 
               GPIO.output(segPins[i], seqs[numList[num]][i]) ## 해당하는 숫자 표기
            time.sleep(0.001)

except KeyboardInterrupt:
   GPIO.cleanup()
