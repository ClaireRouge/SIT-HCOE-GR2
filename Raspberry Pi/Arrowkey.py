import pygame,sys
#import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)
l = (150,150)
d = (150,50)
window = pygame.display.set_mode((10,10))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	l = (150,150)
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		l = (150,50)

	if keys[pygame.K_RIGHT]:
		l = (50,150)

	if keys[pygame.K_UP]:
		print str(l[0]) + " " + str(l[1])
		#ser.write(str(l[0]) + " " + str(l[1]))

	if keys[pygame.K_DOWN]:
		print str(-l[1]) + " " + str(-l[0])
		#ser.write(str(-l[1]) + " " + str(-l[0]))
