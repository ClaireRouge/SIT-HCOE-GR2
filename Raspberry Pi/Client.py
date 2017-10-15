import socket

TCP_IP = '192.168.0.22'    # Static ref file???
TCP_PORT = 313         # Static ref file???
BUFFER_SIZE = 1024       # Static ref file???

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(raw_input())
data = s.recv(BUFFER_SIZE)
print data
s.close()
