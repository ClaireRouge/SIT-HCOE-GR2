import pygame
import sys
import os
import serial

# Pygame terminal fix
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

ser = serial.Serial('/dev/ttyACM0', 115200)

''' Pygame settings '''
# Window settings
l = (150,150)
d = (150,50)
window = pygame.display.set_mode((300,300))

# Joystick init
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
js = joysticks[0]
js.init() # Should be useless

while True:
	for event in pygame.event.get():
		if event.type == pygame.JOYAXISMOTION:
			controllerIn = [
			js.get_axis(0), 	# J1 X Rotation
			js.get_axis(3), 	# J2 Y Crane angle
			js.get_axis(13)-js.get_axis(12)]	# L2-R2 Speed
			speed = 255*controllerIn[2]
			m1 = speed
			m2 = speed
			if (controllerIn[0] < 0):
				m1*=(1 - abs(controllerIn[0]))
			else:
				m2*=(1 - abs(controllerIn[0]))
			print m1, m2
			ser.write(chr(int(m1)/2+128) + chr(int(m2/2+128)))
			ser.readLine()
		elif event.type == pygame.QUIT:
			sys.exit()
