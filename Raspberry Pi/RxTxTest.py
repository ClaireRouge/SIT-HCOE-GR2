import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1:
	ser.write(str(raw_input()))