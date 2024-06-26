import RPi.GPIO as GPIO
import time


# a = 13, b = 26, c = 19, d = 20, e = 21, f = 22, g = 12

segment_pins = [13, 26, 19, 20, 21, 22, 12]

segment_patterns = [
    [0, 0, 0, 0, 0, 0, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 0, 0, 1, 1]   # 9
]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)

def display_number(number):
    pattern = segment_patterns[number]
    for pin, state in zip(segment_pins, pattern):
        GPIO.output(pin, state)

def main():
    try:
        setup()
        while True:
            for number in range(1, 10):
                display_number(number)
                time.sleep(1)
    except KeyboardInterrupt:
        print("")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()

