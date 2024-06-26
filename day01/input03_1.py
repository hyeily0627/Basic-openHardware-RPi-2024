import RPi.GPIO as GPIO
import time

piezo = 5

melody = [261, 293, 329, 349, 391, 440, 493, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo, GPIO.OUT)

Buzz = GPIO.PWM(piezo, 440)

try:
    while True:
        a = int(input("입력(1~8) :  "))
        if 1 <= a <= 8:
            Buzz.start(20)
            Buzz.ChangeFrequency(melody[a - 1])
            time.sleep(0.5)
            Buzz.stop()
        else:
            print("정확한 값 입력!")

except KeyboardInterrupt:
    GPIO.cleanup()