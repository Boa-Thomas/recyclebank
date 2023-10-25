import serial
import serial.tools.list_ports
import time

# Function to list available serial ports
def list_available_serial_ports():
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports found.")
    else:
        print("Available serial ports:")
        for port, desc, hwid in sorted(ports):
            print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")

# Replace with the correct serial port (e.g., '/dev/ttyUSB0')
serial_port = '22'  # Replace 'x' with the correct serial port number
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

    ser = initialize_serial_connection(serial_port, baud_rate)
    if ser:
        try:
            while True:
                data = read_powerbank_data(ser)
                if data:
                    print(f"Powerbank Status: {data}")
                time.sleep(1)
        except KeyboardInterrupt:
            ser.close()
            print("Serial connection closed.")
    else:
        print("Failed to initialize the serial connection. Check your settings.")
