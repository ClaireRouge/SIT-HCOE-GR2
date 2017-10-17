'''
"I must have a prodigious amount of mind;
it takes me as much as a week, sometimes, to make it up!""

- Mark Twain
'''
import pygame as p
import sys
import math
import linecross
import numpy as np
import FearThePoints

size = (720,420)
window = p.display.set_mode(size)
myCar = None
myTrack = None
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
    global myCar,myTrack
    delay = 100
    myTrack = Track()
    myCar = Car((10+75,210))
    while True:
        eventhandle()
        myTrack.draw()
        myCar.draw()
        myCar.updatePos()
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
        p.draw.rect(self.surface,(255,0,0),(0,0,size[0],size[1]),20)
        p.draw.rect(self.surface,(255,0,0),(160,160,400,100))
        self.lines = (
            #outer box
            ((10,10),(710,10)),
            ((10,10),(10,410)),
            ((710,10),(710,410)),
            ((10,410),(710,410)),
            #inner box
            ((160,160),(560,160)),
            ((160,160),(160,260)),
            ((560,160),(560,260)),
            ((160,260),(560,260)),
            )
        #for i in self.lines:
        #    p.draw.line(self.surface,(255,0,255),*i)
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
        self.laser = Laser()
    def getData(self):
        return self.laser.getData(self.pos,self.compass.getData())
    def updatePos(self):
        points = self.getData()
        data = [0]*len(points)
        carDir = self.compass.getData()
        for i,point in enumerate(points):
            #print point
            dist = math.sqrt((point[0]-self.pos[0])**2 + (point[1]-self.pos[1])**2)+0.0000001
            #print (point[1]-self.pos[1]),(point[0]-self.pos[0]),dist
            angle = (1,-1)[point[1]-self.pos[1] > 0]*math.acos((point[0]-self.pos[0])/dist)
            data[i] = (dist,angle)
            #if abs((angle%180) + self.compass.getData())> 90:
            #    print angle%self.compass.getData()
            angle -= carDir
            prevangle = angle
            if angle > math.pi/2+0.2:
                angle -= math.pi*2
            elif angle < -math.pi/2-0.2:
                angle += math.pi*2
            if not -math.pi/2-0.2<angle<math.pi/2+0.2:
                #print prevangle
                #print prevangle, angle, self.compass.getData()
                p.draw.line(window,(255,0,255),self.pos,point)
            p.draw.line(window,(255,0,255),self.pos,point)
        direction = FearThePoints.run(data)
        p2 = [0,0]
        p2[0] = self.pos[0] + math.sin((direction+carDir + math.pi/2))*800
        p2[1] = self.pos[1] + math.cos((direction+carDir + math.pi/2))*800
        p.draw.line(window,(0,255,0),self.pos,p2)

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


class Laser(object):
    def __init__(self):
        self.range = (-math.pi/2,math.pi/2)
        self.steps = 10
    def getData(self,pos,carDir):
        angleRange = (self.range[0] +carDir,self.range[1] +carDir )
        total = float(angleRange[1]-angleRange[0])
        stepResults = [0] * self.steps
        for i in xrange(self.steps):
            direction = total*i/self.steps
            p2 = [0,0]
            p2[0] = pos[0] + math.sin((direction+carDir))*800
            p2[1] = pos[1] + math.cos((direction+carDir))*800
            #print pos,p2
            shortest = sys.maxint
            point = None
            for line in myTrack.lines:
                hitPoint = linecross.calculateIntersectPoint(map(int,pos),map(int,p2),line[0],line[1])
                if hitPoint == None: continue
                dist = (hitPoint[0]-pos[0])**2 +(hitPoint[1]-pos[1])**2
                if dist < shortest:
                    shortest = dist
                    point = hitPoint
            if point != None:
                stepResults[i] = point
            '''
            try:
                p.draw.circle(window,(255,0,255),point,3)
            except:
                print map(int,pos),map(int,p2),i[0],i[1]
                p.draw.line(window,(255,0,255),pos,map(int,p2))
            '''
        for i in xrange(len(stepResults)-1,-1,-1):
            if stepResults[i] == 0:
                del stepResults[i]
        return stepResults


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
        #print c_x,c_y
        try:
            cosV=(c_x/math.sqrt(c_x**2+c_y**2))
            return (1,-1)[c_y > 0]*math.acos(cosV)
        except ZeroDivisionError:
            return 0

if __name__ == "__main__":
    main()
