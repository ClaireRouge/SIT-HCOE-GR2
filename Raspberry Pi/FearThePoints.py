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

        #creating a weight. Can be changed later

        if self.angle != 0:
            self.weight = math.cos(self.angle)*math.sin(self.angle)*angle_dist * 100/self.length
        else:
            self.weight = 0
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
    for point in points:
        direction -= point.weight #go the opposite way

    direction = math.tanh(direction) * math.pi/4
    print direction
    return direction
if __name__ == '__main__':
    run([(1,-90),(1,-30)])
