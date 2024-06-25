from flask import Flask, render_template_string
import RPi.GPIO as GPIO

app = Flask(__name__)

# LED 핀 번호 정의
red_led = 21
blue_led = 26
green_led = 19

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

# 초기 상태를 꺼짐으로 설정
GPIO.output(red_led, True)
GPIO.output(blue_led, True)
GPIO.output(green_led, True)

# HTML 템플릿 정의
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
    <script>
        function controlLED(color, action) {
            fetch("/" + color + "/" + action)
                .then(response => response.text())
                .then(data => {
                    document.getElementById("status").innerText = data;
                });
        }
    </script>
</head>
<body>
    <h1>LED Control</h1>
    <h2>Red LED</h2>
    <button onclick="controlLED('red', 'on')">Turn On</button>
    <button onclick="controlLED('red', 'off')">Turn Off</button>
    <h2>Blue LED</h2>
    <button onclick="controlLED('blue', 'on')">Turn On</button>
    <button onclick="controlLED('blue', 'off')">Turn Off</button>
    <h2>Green LED</h2>
    <button onclick="controlLED('green', 'on')">Turn On</button>
    <button onclick="controlLED('green', 'off')">Turn Off</button>
    <p id="status">LED 상태: 알 수 없음</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/<color>/<action>")
def control_led(color, action):
    led_pins = {
        "red": red_led,
        "blue": blue_led,
        "green": green_led
    }
    
    if color in led_pins:
        if action == "on":
            GPIO.output(led_pins[color], False)
            return f"{color.capitalize()} LED 켜졌어요🚨"
        elif action == "off":
            GPIO.output(led_pins[color], True)
            return f"{color.capitalize()} LED 꺼졌어요"
    return "잘못된 요청"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10111, debug=True)
