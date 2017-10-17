import math
import numpy

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

        self.weight = self.angle*math.cos(self.angle)*self.angle_dist * 10000/self.length**2
        #print self.angle,self.length,self.weight
        #print self.weight, self.angle


def run(point_data):
    """
    point_data: list of touples containing (length,angle)
    """
    if not is_sorted(point_data,1):
        sorted(point_data,key = lambda x:x[1])
    #They are now sorted
    points = get_points(point_data)
    direction = 0 #marks angel of direction
    #k = []
    #for i,v in enumerate(points):
    #    if v.weight > 0:
    #        k.append(i)
    #print k,len(k)
    #k = []
    #for i,v in enumerate(points):
    #    if v.weight < 0:
    #        k.append(i)
    #print k,len(k)
    #print len([x.weight for x in points if x.weight < 0]),len([x.weight for x in points if x.weight > 0])
    right = sum([x.weight for x in points if x.weight < 0])
    left =  sum([x.weight for x in points if x.weight > 0])
    #for point in points:

    nom = (abs(left),abs(right))[abs(left)<abs(right)]
    #print left,right,nom
    denom = (left,right)[abs(left)>abs(right)]
    direction = (nom/denom) * 0.2
    #print direction
    #print direction, "1"

    direction = math.tanh(direction) * math.pi/4
    #print direction, "2"
    return direction
if __name__ == '__main__':
    run([(1,-90),(1,-30)])
