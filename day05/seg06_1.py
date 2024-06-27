import RPi.GPIO as GPIO
import time

segment_pins = [4, 5, 6, 12, 13, 16, 17]
digit_pins = [20, 21, 22, 23]
switch_pin = 25

segment_patterns = [
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

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in digit_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  
    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 占쏙옙占쏙옙치 占쏙옙 占쏙옙占쏙옙

def display_number(number):
    digits = [int(d) for d in str(number).zfill(4)] 
    for i in range(4):
        GPIO.output(digit_pins[i], GPIO.LOW) 
        pattern = segment_patterns[digits[i]]
        for pin, state in zip(segment_pins, pattern):
            GPIO.output(pin, state)
        time.sleep(0.005) 
        GPIO.output(digit_pins[i], GPIO.HIGH)  

def main():
    setup()
    try:
        
        while True:
            if GPIO.input(switch_pin) == GPIO.HIGH:   
                display_number(1234)
            else:
                display_number(0000)
    except KeyboardInterrupt:
        print("")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
