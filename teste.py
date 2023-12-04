import serial
import requests
import time

# Replace '/dev/ttyUSB0' with your Arduino's serial port.
serial_port = '/dev/ttyUSB0'
baud_rate = 9600

# URL of the web server endpoint where you want to send the data.
post_url = 'http://yourserver.com/post-endpoint'

# Set up the serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)
ser.flush()

# Variables to store the latest voltage and current values
input_voltage = None
input_current = None

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        # Check if the line contains 'Input Voltage' or 'Input Current'
        if "Input Voltage" in line:
            # Parse the voltage value and store it in the variable
            input_voltage = float(line.split('=')[1].strip())
            print(f"Stored voltage value: {input_voltage} V")
        elif "Input Current" in line:
            # Parse the current value and store it in the variable
            input_current = float(line.split('=')[1].strip())
            print(f"Stored current value: {input_current} A")

        # Send a POST request to the server with the voltage and current values
        if input_voltage is not None and input_current is not None:
            data = {'voltage': input_voltage, 'current': input_current}
            response = requests.post(post_url, data=data)
            print(f"Response from server: {response.text}")

            # Reset the variables and add a delay to limit the number of requests
            input_voltage = None
            input_current = None
            time.sleep(10)  # Adjust the delay as needed
