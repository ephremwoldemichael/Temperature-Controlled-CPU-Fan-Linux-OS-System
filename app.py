from flask import Flask, render_template
import time

app = Flask(__name__)

def read_file(filename, default='N/A'):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except:
        return default

@app.route('/')
def home():
    temp = read_file("temperature.txt", "Unknown")
    status = read_file("fan_status.txt", "Unknown")
    timestamp = time.strftime("%H:%M:%S")
    return render_template("dashboard.html", temp=temp, status=status, time=timestamp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

