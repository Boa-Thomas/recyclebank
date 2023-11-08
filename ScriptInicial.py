import RPi.GPIO as GPIO
import spidev
import time
import serial
import requests  # For the webserver



# Initialize SPI device
spi = spidev.SpiDev()
spi.open(0, 0)

# Function to read voltage data from a separate module connected to SPI channel 0
def read_voltage(channel):
    # Modify this to read voltage data from your specific voltage module
    # The following line is just a placeholder:
    voltage_data = spi.xfer2([1, (8 + channel) << 4, 0])
    voltage = ((voltage_data[1] & 3) << 8) + voltage_data[2]
    return voltage

# Function to read current data from a separate module connected to SPI channel 1
def read_current(channel):
    # Modify this to read current data from your specific current module
    # The following line is just a placeholder:
    current_data = spi.xfer2([1, (8 + channel) << 4, 0])
    current = ((current_data[1] & 3) << 8) + current_data[2]
    return current

# Function to calculate voltage from sensor reading
def get_voltage(data, reference=3.3):
    voltage = (data / 1023.0) * reference
    return voltage

# Function to calculate current from sensor reading
def get_current(data, reference=3.3):
    voltage = (data / 1023.0) * reference
    current = voltage  # Modify this to convert sensor output to current value
    return current

# Function to actuate H-bridge
def actuate_h_bridge(state):
    if state == "FORWARD":
        GPIO.output(17, True)
        GPIO.output(18, False)
        GPIO.output(22, True)
        GPIO.output(23, False)
    elif state == "REVERSE":
        GPIO.output(17, False)
        GPIO.output(18, True)
        GPIO.output(22, False)
        GPIO.output(23, True)
    else:  # STOP or anything else
        GPIO.output(17, False)
        GPIO.output(18, False)
        GPIO.output(22, False)
        GPIO.output(23, False)

# Function to control the relay
def control_relay(state):
    GPIO.output(24, state)  # GPIO pin 24 controls the relay

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Define the URL of your web server
server_url = "http://example.com/api/endpoint"

try:
    while True:
        # Read voltage and current from separate modules
        voltage_data = read_voltage(0)  # Assuming voltage on channel 0
        current_data = read_current(1)  # Assuming current on channel 1

        voltage = get_voltage(voltage_data)
        current = get_current(current_data)

        print(f"Voltage: {voltage}V, Current: {current}A")

        # Create a dictionary with the data to post
        data_to_post = {
            "voltage": voltage,
            "current": current
        }

        # Post data to the web server
        response = requests.post(server_url, json=data_to_post)
        if response.status_code == 200:
            print("Data sent successfully.")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")

        # Read keyboard input for actuation
        user_input = input("Do you want to actuate the H-bridge? (yes/no): ")

        if user_input.lower() == 'yes':
            actuate_h_bridge("FORWARD")
            control_relay(True)  # Turn on the relay
        elif user_input.lower() == 'no':
            actuate_h_bridge("STOP")
            control_relay(False)  # Turn off the relay

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting.")