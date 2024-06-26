import RPi.GPIO as GPIO
import time

segment_pins = [24, 5, 6, 12, 13, 16, 17]
digit_pins = [20, 21, 22, 23]

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
    for pin in digit_ins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  

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
        for number in range(1, 10000):
            start_time = time.time()
            while time.time() - start_time < 0.5: 
                display_number(number)
    except KeyboardInterrupt:
        print("")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()