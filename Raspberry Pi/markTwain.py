'''
"I must have a prodigious amount of mind;
it takes me as much as a week, sometimes, to make it up!""

- Mark Twain
'''
import pygame as p
import sys
size = (720,420)
window = p.display.set_mode(size)

def eventhandle():
    for event in p.event.get():
		if event.type == p.QUIT:
			sys.exit()

class track(object):
    def __init__(self):
        self.surface = p.Surface(size)
        self.surface.fill((0,0,0))
        p.draw.rect(self.surface,(255,0,0),(0,0,size[0],size[1]),10)
        p.draw.rect(self.surface,(255,0,0),(160,160,400,100))
    def draw(self):
        window.blit(self.surface,(0,0))



if __name__ == "__main__":

    delay = 1000
    window = p.display.set_mode(size)
    mytrack = track()

    while True:
        eventhandle()
        mytrack.draw()

        p.display.flip()
        p.time.wait(delay)
