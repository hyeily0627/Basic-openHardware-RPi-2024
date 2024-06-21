import RPi.GPIO as GPIO
import time

led = 21

# GPIO BCM 모드로 설정 
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정 (입력/출력)
GPIO.setup(led, GPIO.OUT)

try:
    while(1):
        GPIO.output(led,False)

except KeyboardInterrupt: # Ctrl + c 를 누르면 GPIO를 종료시킴
    GPIO.cleanup()
