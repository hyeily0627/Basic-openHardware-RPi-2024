import RPi.GPIO as GPIO

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

	seq = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0]
    ]

try:
	while 1:
		for stepPin in range(0,4):
			moter = steps[stepPin]

except KeyboardInterrupt:
	GPIO.cleanup()

#강사님 코드 안도는데 ㅠ
