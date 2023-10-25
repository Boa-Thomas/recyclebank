import RPi.GPIO as GPIO
import spidev
import time

# Initialize SPI device
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
def read_spi(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Function to calculate voltage
def get_voltage(data, reference=3.3):
    return (data / 1023.0) * reference

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
    else: # STOP or anything else
        GPIO.output(17, False)
        GPIO.output(18, False)
        GPIO.output(22, False)
        GPIO.output(23, False)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

try:
    while True:
        # Read voltage and current from ADC (assuming voltage is on channel 0 and current on channel 1)
        voltage_data = read_spi(0)
        current_data = read_spi(1)
        
        voltage = get_voltage(voltage_data)
        current = get_voltage(current_data)  # Add calculation based on your current sensor
        
        print(f"Voltage: {voltage}V, Current: {current}A")
        
        # Actuate H-bridge based on some condition (replace with your own logic)
        if voltage > 2.5:
            actuate_h_bridge("FORWARD")
        else:
            actuate_h_bridge("STOP")
        
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting.")
