from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        h1 { color: #333; }
        form { margin-top: 20px; }
        label, input { font-size: 16px; }
        input[type=number] { width: 80px; padding: 5px; margin-right: 10px; }
        input[type=submit] { padding: 5px 15px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
        input[type=submit]:hover { background-color: #0056b3; }
        .feedback { margin-top: 20px; font-size: 18px; color: green; }
    </style>
</head>
<body>
    <h1>LED Brightness Control</h1>
    <form method="POST">
        <label for="brightness">Set LED Brightness (0-255): </label>
        <input type="number" id="brightness" name="brightness" min="0" max="255">
        <input type="submit" value="Set Brightness">
    </form>
    {% if message %}
    <p class="feedback">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

SERVER_IP = "http://172.30.1.177:5000"  # Arduino 서버 IP

def set_led_brightness(server_ip, brightness):
    try:
        if 0 <= brightness <= 255:
            url = f"{server_ip}/?brightness={brightness}"
            response = requests.get(url)
            if response.status_code == 200:
                return "Brightness updated successfully!"
            else:
                return f"Failed to update brightness. HTTP Status Code: {response.status_code}"
        else:
            return "Brightness value must be between 0 and 255."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

@app.route("/", methods=["GET", "POST"])
def control_led():
    message = None
    if request.method == "POST":
        try:
            brightness = int(request.form["brightness"])
            message = set_led_brightness(SERVER_IP, brightness)
        except ValueError:
            message = "Please enter a valid integer value."
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
