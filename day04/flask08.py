from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, True) # 꺼진 상태

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/on")
def led_on():
    GPIO.output(led, False)
    return "LED ON"

@app.route("/off")
def led_off():
    GPIO.output(led, True)
    return "LED OFF"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10111, debug=True)
