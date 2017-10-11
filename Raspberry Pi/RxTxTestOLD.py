import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1:
	ser.write(chr(map(int,raw_input().split())))