import RPi.GPIO as IO        
import time

IO.setwarnings(False)        
IO.setmode (IO.BCM)       

pin = [4, 5, 6, 12, 13, 16, 17]

for a in pin:
    IO.setup(a,IO.OUT)          

list =[

    [0,0,1,1,1,1,1,1],   #0
    [0,0,0,0,0,1,1,0],   #1
    [0,1,0,1,1,0,1,1],   #2
    [0,1,0,0,1,1,1,1],   #3
    [0,1,1,0,0,1,1,0],   #4
    [0,1,1,0,1,1,0,1],   #5
    [0,1,1,1,1,1,0,1],   #6
    [0,0,0,0,0,1,1,1],   #7
    [0,1,1,1,1,1,1,1],   #8
    [0,1,1,0,0,1,1,1],   #9
       ]

def Display(num):
    y=0
    #각 자리의 숫자 추출
    fnd = [0,0,0,0]
    fnd[0]=int((num/100)/10)
    fnd[1]=int((num/100)%10)
    fnd[2]=int((num%100)/10)
    fnd[3]=int((num%100)%10)

   
    # 자리에 맞는 숫자 출력
    for i in range(4): 
        if y==0:
            d=fnd[y] #해당 자리의 숫자배열 출력
            for j in pin[3:]:
                if y+7==j:
                    IO.output(j,IO.LOW)   #자리에 해당하는 fnd on
                else :
                    IO.output(j,IO.HIGH)
        elif y==1:
            d=fnd[y]
            for j in pin[3:]:
                if y+7==j:
                    IO.output(j,IO.LOW)
                else :
                    IO.output(j,IO.HIGH)
        elif y==2:
            d=fnd[y]
            for j in pin[3:]:
                if y+7==j:
                    IO.output(j,IO.LOW)
                else :
                    IO.output(j,IO.HIGH)
        elif y==3:
            d=fnd[y]
            for j in pin[3:]:
                if y+7==j:
                    IO.output(j,IO.LOW)
                else :
                    IO.output(j,IO.HIGH)
        else :
            for k in pin[3:]:
                IO.output(k,IO.HIGH)

      # 숫자 원형 출력
        for x in list[d]:
            IO.output(4,x)            # 데이터 비트 넣기
            IO.output(5,1)            # 클럭 핀 HIGH
            IO.output(5,0)            # 클러 핀 LOW RISING엣지에 넣기
            IO.output(4,0)            # 데이터 비트 초기화
            IO.output(6,1)            # 8비트 병렬로 쉬프트 하기
            IO.output(6,0)            # 쉬프트 핀 LOW

        y+=1

        time.sleep(0.5) #빠르기 조절

try:
    while 1:
            Display(1234)   #원하는 숫자

except KeyboardInterrupt:
    IO.cleanup()
