import RPi.GPIO as GPIO
import time

red = 21
blue = 5
green = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try :
    while (True) :
        GPIO.output(red, False)
        time.sleep(1) 
        GPIO.output(red, True)
        time.sleep(1)

        GPIO.output(blue, False)
        time.sleep(1) 
        GPIO.output(blue, True)
        time.sleep(1)

        GPIO.output(green, False)
        time.sleep(1) 
        GPIO.output(green, True)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
