import serial
import time

port = 'COM3'
baud_rate = 9600
try:
    ser = serial.Serial(port, baud_rate, timeout=1)
    print(f"Connected to {port} at {baud_rate} baud.")
    message = "Hello Arduino!\n" \
            ser.write(message.encode('utf-8'))
    print(f"Sent: {message.strip()}")
    time.sleep(1)
    if ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(f"Received: {response}")
    ser.close()
    print("Connection closed.")
except serial.SerialException as e:
    print(f"Error: {e}"