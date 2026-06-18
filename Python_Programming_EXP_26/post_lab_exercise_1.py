import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)  # Update COM port
time.sleep(2)  # Allow time for connection setup

while True:
    command = input("Enter command (ON/OFF): ").strip()
    if command in ["ON", "OFF"]:
        ser.write((command + '\n').encode())  # Send command
        print(f"Sent: {command}")
    else:
        print("Invalid command. Enter ON or OFF.")

ser.close()
