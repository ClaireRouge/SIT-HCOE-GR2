import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1:
	s = map(int,raw_input().split())
	ser.write(chr(s[0])+chr(s[1]))