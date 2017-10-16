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
        self.weight = angle_dist * 1/(self.length**2) * 1/self.angle
        print self.weight, self.angle


def run(point_data):
    """
    point_data: list of touples containing (length,angle)
    """
    if not is_sorted(point_data,1):
        raise NotImplementedError
    #They are now sorted
    points = get_points(point_data)
    direction = 0 #marks angel of direction
    for point in points:
        direction -= point.weight #go the opposite way
    print direction

run([(1,-90),(1,-30)])
