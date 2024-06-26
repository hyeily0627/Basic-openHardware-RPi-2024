import RPi.GPIO as GPIO
import time

switch = 25
com_pins = [20, 21, 22, 23]
led_pin = [4, 5, 6, 12, 13, 16, 17]
# a 4(빨강), b 5(갈색), c 6(초록)
#d 12(파랑), e 13(회색), f 16(검정), g 17(흰색) 

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for ledPin in led_pin:
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, True)
	
num = [[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
				[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],
				[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]