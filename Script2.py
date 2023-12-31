import serial
import os
import time

# Function to list available serial ports
def list_available_serial_ports():
    ports = [f for f in os.listdir('/dev/') if f.startswith('ttyS') or f.startswith('ttyUSB')]
    if not ports:
        print("No serial ports found.")
    else:
        print("Available serial ports:")
        for port in ports:
            print(f"Port: /dev/{port}")

# Replace with the correct serial port (e.g., '/dev/ttyUSB0')
serial_port = '/dev/ttyUSB0'  # Replace with the correct serial port
baud_rate = 9600

def initialize_serial_connection(port, baud):
    try:
        ser = serial.Serial(port, baud)
        return ser
    except Exception as e:
        print(f"Error: {e}")
        return None

def read_powerbank_data(ser):
    try:
        data = ser.readline().decode().strip()
        return data
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

if __name__ == '__main__':
    # List available serial ports
    list_available_serial_ports()

    serial_connection = initialize_serial_connection(serial_port, baud_rate)
    if serial_connection:
        try:
            while True:
                data = read_powerbank_data(serial_connection)
                if data:
                    print(f"Powerbank Status: {data}")
                time.sleep(1)
        except KeyboardInterrupt:
            serial_connection.close()
            print("Serial connection closed.")
    else:
        print("Failed to initialize the serial connection. Check your settings.")
