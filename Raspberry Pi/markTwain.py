'''
"I must have a prodigious amount of mind;
it takes me as much as a week, sometimes, to make it up!""

- Mark Twain
'''
import pygame as p
import sys
import math
import MakeAChoice
import numpy as np
size = (720,420)
window = p.display.set_mode(size)
myCar = None
def eventhandle():
    for event in p.event.get():
		if event.type == p.QUIT:
			sys.exit()
    keys=p.key.get_pressed()
    x = 0
    y = 0
    gotIn = False
    if keys[p.K_UP]:
        y -= 5
        gotIn = True
    if keys[p.K_DOWN]:
        y += 5
        gotIn = True
    if keys[p.K_LEFT]:
        x -= 5
        gotIn = True
    if keys[p.K_RIGHT]:
        x += 5
        gotIn = True
    if gotIn:
        myCar.pos = myCar.pos[0] + x,myCar.pos[1] + y

def main():
    global myCar
    delay = 50
    mytrack = Track()
    myCar = Car((10+75,210))
    while True:
        eventhandle()
        mytrack.draw()
        myCar.draw()
        myCar.printdata()
        p.display.flip()
        p.time.wait(delay)


class Line(object):
    def __init__(point1,point2):
        pass


#The track the car drives on
class Track(object):
    def __init__(self):
        self.surface = p.Surface(size)
        self.surface.fill((0,0,0))
        p.draw.rect(self.surface,(255,0,0),(0,0,size[0],size[1]),10)
        p.draw.rect(self.surface,(255,0,0),(160,160,400,100))
    def draw(self):
        window.blit(self.surface,(0,0))

class Car(object):
    posX = 0
    posY = 1
    def __init__(self,pos):
        #force floats as pos
        self.pos = map(float,pos)
        self.compass = Compass(self)
        #currently always faces upwards
        self.prevPos = [(pos[self.posX],pos[self.posY]-1)]

    def pos():
        doc = "The pos property."
        def fget(self):
            return self._pos
        def fset(self, value):
            try:
                self.prevPos.insert(0,self._pos)
                if len(self.prevPos) > 5:
                    del self.prevPos[-1]
            except AttributeError:
                pass
            self._pos = value
        def fdel(self):
            del self._pos
        return locals()
    pos = property(**pos())

    def draw(self):
        p.draw.circle(window,(0,255,255),map(int,self.pos),5)
        for i in range(len(self.prevPos)):
            p.draw.circle(window,(0,128/(i/2+1),128/(i/2+1)),map(int,self.prevPos[i]),5)

    def printdata(self):
        print self.compass.getData()
class Compass(object):
    def __init__(self,car):
        #create fictive pos based on car pos
        self.car = car
    def getData(self):
        a_x,a_y = self.car.pos
        b_x,b_y = self.car.prevPos[-1]
        #vektor b->a
        c_x,c_y = a_x-b_x, a_y-b_y
        #angle between vectors
        print c_x,c_y
        try:
            cosV=(c_x/math.sqrt(c_x**2+c_y**2))
            return (1,-1)[c_y > 0]*math.acos(cosV)/math.pi*180
        except ZeroDivisionError:
            return 0

if __name__ == "__main__":
    main()
