import math
import numpy
import pygame

corner_counter = 0
CORNER_MAX = 100
PRE_TANH_COEFF = 0.08
CORNER_WEIGHT = 0.004
START_DIRECTION = -1
PART_BACKWARD = 2.5
SPEEDCOEF = 0.3
MAX_SPEED = 0.3

def is_sorted(target,sortnum):
    for index,value in enumerate(target):
        if value[sortnum] < target[index-1][sortnum] and index != 0:
            return False
    return True
#factory
def get_points(point_data):
    points = [0] * len(point_data)

    points[0] = Point(float(point_data[1][1]-point_data[0][1]),*point_data[0])

    for i in xrange(1,len(point_data)-1):
        points[i] = Point(float(point_data[i+1][1]-point_data[i-1][1]),*point_data[i])

    last_point_data = len(point_data) -1
    points[last_point_data] = Point(float(point_data[last_point_data][1]-point_data[last_point_data-1][1]),*point_data[last_point_data])

    return points


class Point(object):
    def __init__(self,angle_dist,length,angle):
        self.angle = float(angle)
        self.length = float(length)
        self.angle_dist = abs(angle_dist)
        #print angle
        #creating a weight. Can be changed later

        self.weight = self.angle*math.cos(self.angle)*self.angle_dist * 10000000/self.length**4
        #print self.angle,self.length,self.weight
        #print self.weight, self.angle


def run(point_data):
    """
    point_data: list of touples containing (length,angle)
    returns a tuple containing (speed,angle)
    angle in radians
    speed as a fraction of total speed
    """
    global corner_counter
    points = get_points(point_data)

    right = sum([x.weight for x in points if x.weight < 0])
    left =  sum([x.weight for x in points if x.weight > 0])
    right *= 1.0
    left *= 1.3
    print left,right
    nom = (abs(left),abs(right))[abs(left)<abs(right)]
    denom = (left,right)[abs(left)>abs(right)]
    direction = (nom/denom) * PRE_TANH_COEFF
    softsign_x =  SPEEDCOEF/(abs(left)+abs(right))
    speed = softsign_x/(1+abs(softsign_x))*MAX_SPEED
    '''
    if left > CORNER_WEIGHT and right < -CORNER_WEIGHT and direction < 2*PRE_TANH_COEFF and corner_counter == 0: #determined by testing

        corner_counter = CORNER_MAX
        #pygame.time.wait(2000)
        #print corner_counter
    if corner_counter != 0:
        #its in a cornor
        speed = -0.25
        if CORNER_MAX-corner_counter < CORNER_MAX/PART_BACKWARD:
            direction = 0
            #print "hi",direction
        else:
            direction = START_DIRECTION
            #print "hello",direction
        corner_counter -= 1
    else:'''
    direction = math.tanh(direction)
    #sprint abs(left),abs(right)
    print speed,direction
    return speed,direction

if __name__ == '__main__':
    run([(1,-90),(1,-30)])
