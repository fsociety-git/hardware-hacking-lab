import serial
import argparse

def uart_communicate(port, baudrate=115200):
    ser = serial.Serial(port, baudrate, timeout=1)
    print("UART connected. Type commands; Ctrl+C to exit.")
    try:
        while True:
            command = input("> ")
            ser.write(command.encode() + b'\n')
            response = ser.readline().decode().strip()
            print(response)
    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UART Interface")
    parser.add_argument("--port", required=True, help="Serial port (e.g., /dev/ttyUSB0)")
    parser.add_argument("--baud", default=115200, type=int, help="Baud rate")
    args = parser.parse_args()
    uart_communicate(args.port, args.baud)
