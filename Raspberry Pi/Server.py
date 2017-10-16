import socket
import serial

''' TCP Settings '''
TCP_IP = '192.168.0.22'    # Static ref file???
TCP_PORT = 313         # Static ref file???
BUFFER_SIZE = 256       # Static ref file???

# Serial begin						Baud rate
ser = serial.Serial('/dev/ttyACM0', 115200)

# TCP init
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

while True:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	controllerIn = map(float, data.split())
	speed = 255*controllerIn[2]
	m1 = speed
	m2 = speed
	if (controllerIn[0] < 0):
		m1*=(1 - abs(controllerIn[0]))
	else:
		m2*=(1 - abs(controllerIn[0]))
	print m1, m2
	ser.write(chr(int(m1)/2+128) + chr(m2/2+128))
	conn.send("1")
conn.close()
