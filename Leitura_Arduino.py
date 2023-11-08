import serial

# Replace '/dev/ttyACM0' with the serial port that your Arduino is connected to.
# The baud rate should be set to the same rate you've set in your Arduino program (usually in Serial.begin()).
serial_port = '/dev/ttyACM0'
baud_rate = 9600

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
