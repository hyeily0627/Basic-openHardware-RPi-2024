import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for step in steps:
    GPIO.setup(step, GPIO.OUT)
    GPIO.output(step, 0)

try:
    step_sequence = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
    ]

    while True:
        for step in step_sequence:
            for pin in range(4):
                GPIO.output(steps[pin], step[pin])
            time.sleep(0.01)

except KeyboardInterrupt:
    GPIO.cleanup()

