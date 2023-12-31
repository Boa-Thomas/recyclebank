import serial

# Initialize serial port
ser = serial.Serial('/dev/ttyACM0', 9600)

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
