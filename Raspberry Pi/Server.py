import socket

# This part listens on the TCP_PORT for a message from the Gateway

TCP_IP = '192.168.0.22'    # Static ref file???
TCP_PORT = 313         # Static ref file???
BUFFER_SIZE = 256       # Static ref file???

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
while True:
	print "Kage1"
	s.listen(1)
	print "Kage2"
	conn, addr = s.accept()
	data = conn.recv(BUFFER_SIZE)
	print "Kage3"
	if not data: break
	print data
	#conn.send(data)
conn.close()
