import RPi.GPIO as GPIO
import time

segment_pins = [13, 26, 19, 20, 21, 22, 12]
button = 4

segment_patterns = [
    [0, 0, 0, 0, 0, 0, 0],  # 0
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
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def display_number(number):
    pattern = segment_patterns[number]
    for pin, state in zip(segment_pins, pattern):
        GPIO.output(pin, state)

def main():
    try:
        setup()
        current_number=0
        display_number(current_number)
        last_button_state = GPIO.input(button)
        while True:
            button_state = GPIO.input(button)
            if GPIO.input(button) == GPIO.HIGH and last_button_state == GPIO.LOW:
                current_number = (current_number + 1) % 10  # Increment and wrap around after 9
                display_number(current_number)
                print(f"Displayed number: {current_number}")
                time.sleep(0.5)
            last_button_state = button_state
            time.sleep(0.001)
    except KeyboardInterrupt:
        print("")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
        

