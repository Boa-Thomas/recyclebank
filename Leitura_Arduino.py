import serial

# Initialize serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        sensor1_value, sensor2_value = map(int, line.split(","))
        
        # Now you can use sensor1_value and sensor2_value as you wish
        print(f"Sensor 1: {sensor1_value}, Sensor 2: {sensor2_value}")
