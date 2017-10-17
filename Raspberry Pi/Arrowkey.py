import pygame,sys
#import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)
l = (150,150)
d = (150,50)
window = pygame.display.set_mode((300,300))

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
js = joysticks[0]
js.init()

print joysticks

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print "KAGE"
			if event.key == pygame.K_LEFT:
				print "LEFT"
			if event.key == pygame.K_RIGHT:
				print "RIGHT"
		if event.type == pygame.JOYAXISMOTION:
			print str(js.get_axis(0)) # J1 X
			print str(js.get_axis(3)) # J2 Y
			print str(js.get_axis(2)) # L2-R2
		elif event.type == pygame.QUIT:
			sys.exit()
