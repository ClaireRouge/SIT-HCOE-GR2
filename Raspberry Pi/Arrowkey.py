import pygame,sys
#import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def getKey():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return "up"
        elif k=='\x1b[B':
                return "down"
        elif k=='\x1b[C':
                return "right"
        elif k=='\x1b[D':
                return "left"
l = (150,150)
d = (150,50)
window = pygame.display.set_mode((10,10))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	l = (150,150)
	keys = pygame.key.get_pressed()
	k = get()
	if k == "up":
		l = (150,50)

	if k == "down":
		l = (50,150)

	if k == "left":
		print str(l[0]) + " " + str(l[1])
		#ser.write(str(l[0]) + " " + str(l[1]))

	if k == "right":
		print str(-l[1]) + " " + str(-l[0])
		#ser.write(str(-l[1]) + " " + str(-l[0]))
