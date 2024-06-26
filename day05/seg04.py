import RPi.GPIO as GPIO
import time

switch = 4
led = [13, 26, 19, 20, 21, 22, 12]

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led = [13, 26, 19, 20, 21, 22, 12]

for ledPin in led:
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, False)  # LED를 끄고 시작

num = [[0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1],
       [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1],
       [1, 1, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]

current_num = 0

def button_callback(channel):
    global current_num
    current_num = (current_num + 1) % len(num)  # 숫자 증가 및 순환

try:
    # 이벤트 감지 설정
    GPIO.add_event_detect(switch, GPIO.FALLING, callback=button_callback, bouncetime=300)
    while True:
        for pin in range(7):
            GPIO.output(led[pin], num[current_num][pin])
        time.sleep(0.1)  # 루프 딜레이

except RuntimeError as e:
    print(f"RuntimeError: {e}")
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()

