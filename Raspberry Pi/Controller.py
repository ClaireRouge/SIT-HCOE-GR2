import pygame
import sys
import socket

''' Pygame settings '''
# Window settings
l = (150,150)
d = (150,50)
window = pygame.display.set_mode((300,300))

''' TCP/Socket Settings '''
TCP_IP = ' fe80::ba27:ebff:fee0:2f83'	# This IP should be static and needs to be the same client and servervise
TCP_PORT = 313
BUFFER_SIZE = 32			# How much space the buffer should use, for faster response, decrease this number


# Joystick init
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
js = joysticks[0]
js.init() # Should be useless

# TCP init
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
	for event in pygame.event.get():
		if event.type == pygame.JOYAXISMOTION:
			s.send(str(js.get_axis(0)) + " " +	# J1 X Rotation
			str(-js.get_axis(3)) + " " +			# J2 Y Crane angle
			str(-js.get_axis(2)))				# L2-R2 Speed
			s.recv(BUFFER_SIZE)
		elif event.type == pygame.QUIT:
			sys.exit()
