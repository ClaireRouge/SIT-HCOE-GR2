import pygame,sys
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
s = "000 000"
window = pygame.display.set_mode((10,10))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				#print "hi"
				ser.write(s)
			if event.key == pygame.K_a:
				s = raw_input("Input motor:\n")
				#print s, "was inputted"
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				#print "hi again",s
				ser.write("000 000")
