import RPi.GPIO as GPIO
import time

red_led = 21
blue_led = 20
green_led = 16

# GPIO BCM 모드로 설정 
GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정 (입력/출력)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

try:
    while(1):
        # red_led ON
        GPIO.output(red_led,False)
        GPIO.output(blue_led, True)
        GPIO.output(green_led, True)
        time.sleep(1)

        # blue_led ON
        GPIO.output(red_led, True)
        GPIO.output(blue_led, False)
        GPIO.output(green_led, True)
        time.sleep(1)

        # green_led ON
        GPIO.output(red_led, True)
        GPIO.output(blue_led, True)
        GPIO.output(green_led, False)
        time.sleep(1)

except KeyboardInterrupt: # Ctrl + c 를 누르면 GPIO를 종료시킴
    GPIO.cleanup()
