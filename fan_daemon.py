import time
import random  # Simulates temperature sensor reading
import logging

# Set up logging
logging.basicConfig(
    filename='/var/log/fan_daemon.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fan threshold
TEMP_THRESHOLD = 40  # degrees Celsius

def read_temperature():
    # Replace this with actual sensor reading in real project
    return random.uniform(30.0, 50.0)

def control_fan(temp):
    if temp > TEMP_THRESHOLD:
        logging.info(f"Temperature: {temp:.2f}°C - Fan ON")
        print("Fan ON")
        # Add GPIO logic to turn on fan here
    else:
        logging.info(f"Temperature: {temp:.2f}°C - Fan OFF")
        print("Fan OFF")
        # Add GPIO logic to turn off fan here

def main():
    while True:
        temperature = read_temperature()
        control_fan(temperature)
        time.sleep(5)

if __name__ == '__main__':
    main()

