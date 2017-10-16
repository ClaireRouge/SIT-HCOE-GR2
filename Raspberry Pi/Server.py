import socket

# This part listens on the TCP_PORT for a message from the Gateway

TCP_IP = '192.168.0.22'    # Static ref file???
TCP_PORT = 313         # Static ref file???
BUFFER_SIZE = 1024       # Static ref file???

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
while True:
	s.listen(1)
	conn, addr = s.accept()
	data = conn.recv(BUFFER_SIZE)
	print data
	#conn.send(data)
	conn.close()
