from flask import Flask, render_template_string
import RPi.GPIO as GPIO

app = Flask(__name__)

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, True) # 꺼진 상태

# html 템플릿 
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
    <script>
        function controlLED(action) {
            fetch("/" + action)
                .then(response => response.text())
                .then(data => {
                    document.getElementById("status").innerText = data;
                });
        }
    </script>
</head>
<body>
    <h1>LED Control</h1>
    <button onclick="controlLED('on')">Turn On</button>
    <button onclick="controlLED('off')">Turn Off</button>
    <p id="status">LED 상태: 알 수 없음</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/on")
def led_on():
    GPIO.output(led, False)
    return "불 켜짐 상태🚨"

@app.route("/off")
def led_off():
    GPIO.output(led, True)
    return "불 꺼짐 상태"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10111, debug=True)
