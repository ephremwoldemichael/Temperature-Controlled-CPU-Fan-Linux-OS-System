# 🌀 Temperature-Controlled Fan Daemon with Web Dashboard

A mini embedded Linux simulation project that:

- Reads temperature input (`temperature.txt`)
- Turns fan ON/OFF based on thresholds
- Writes fan status to `fan_status.txt`
- Shows real-time status via a Flask web dashboard

## 📁 Project Structure


fan_daemon.cpp → C++ daemon controlling fan temperature.txt → Input (simulated sensor) fan_status.txt → Output status (ON/OFF) app.py → Flask dashboard templates/dashboard.html → UI template requirements.txt → Python dependencies

## ⚙️ How It Works

1. C++ daemon checks `temperature.txt` every 5s
2. Based on thresholds (≥ 60°C ON, ≤ 45°C OFF), updates `fan_status.txt`
3. Flask app shows dashboard with live status & updates every 5 seconds

## 🚀 Run It Locally

### Prerequisite (Python + Flask):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

