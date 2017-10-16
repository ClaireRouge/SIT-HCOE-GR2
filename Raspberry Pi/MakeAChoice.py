import math,numpy
import sys
class Track:
    """
    Class to make an estimated guess on the position of the robot
    """
    def Update(self, arg):
        pass

class Line:
    def __init__(self, vecs):
        x_bar = 0.0
        y_bar = 0.0
        xi = []
        yi = []
        for vec in vecs:
            x_bar += vec.i
            y_bar += vec.j
            xi.append(vec.i)
            yi.append(vec.j)
        x_bar /= len(vecs)
        y_bar /= len(vecs)
        denom = nom = 0.0
        for i in range(len(vecs)):
            nom += (yi[i]-y_bar)*(xi[i]-x_bar)
            denom += (xi[i]-x_bar)**2
        self.a = nom/denom
        self.b = y_bar - self.a*x_bar
        self.f = lambda x: self.a*x+self.b
        SS_tot = sum([(y - y_bar)**2 for y in yi])
        SS_res = sum([(y_bar-self.f(xi[i]))**2 for i in range(len(yi))])

        self.r2 = 1-SS_res/SS_tot
        


class Vector:
    def __init__(self,xcord,ycord):
        self.i = xcord
        self.j = ycord
    def lengthSQ(self):
        return i**2 + j**2


def decide(direction,data):
    """
    Main function for deciding which way to drive
    Data is a 2d tuple on the form
    (
        (time,direction,distance)
        ...
            ...
    )
    """
    pass




if __name__ == "__main__":
    k = [[2,3],[2,4],[2,5]]
    vecs = [Vector(*i) for i in k]
    line = Line(vecs)
    print line.r2,line.a,line.b
