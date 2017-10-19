import FearThePoints
import math

def main():
    data = list(getData())
    data = map(lambda x: (x[0],x[1]/180.0*math.pi),data)
    direction = FearThePoints.run(data)

    m1 = 255 - int(255*direction)
    m2 = 255 - int(-255*direction)
    send(m1,m2)

def send(m1,m2):
    pass

def getData():
    pass

if __name__ == '__main__':
    main()
