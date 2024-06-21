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
        GPIO.output(blue, False)
        GPIO.output(green, False)
        time.sleep(1) # RED!

        GPIO.output(red, False)
        GPIO.output(blue, False)
        GPIO.output(green, True)
        time.sleep(1) # GREEN!

        GPIO.output(red, False)
        GPIO.output(blue, True)
        GPIO.output(green, False)
        time.sleep(1) # BLUE!        

except KeyboardInterrupt:
    GPIO.cleanup() #ctrl + c
