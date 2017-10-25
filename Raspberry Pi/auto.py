import FearThePoints
import math
import serial
import struct
import time
#SERIAL STUFF
ser = serial.Serial('/dev/ttyACM0', 115200)

data = []

def main():

    time.sleep(3) #make sure arduino has collected data
    send(0,0)
    data = []
    while True:
        newData = getData()
        if newData != []:
            data.extend(newData)

            for i in xrange(len(data)-2,0,-1): #starts at next to last element
                print i
                if data[i][1] == newData[-1][1] and data[i-1][1] == newData[-2][1]:
                    data = data[i+1:]
                    break
        print data
        senddata = map(lambda x: (x[0],x[1]/180.0*math.pi),data)
        direction = FearThePoints.run(senddata)
        m1 = (128 - int(128*math.sin(direction)))*(1,-1)[math.cos(direction) < 0]
        m2 = (128 - int(-128*math.sin(direction)))*(1,-1)[math.cos(direction) < 0]
        #print m1,m2
        send(m1,m2)

def send(m1,m2):
    print "wrote:", chr(int(m1)/2+128) + chr(int(m2/2+128))
    ser.write(chr(int(m1)/2+128) + chr(int(m2/2+128)))

def getData():
    nrbytes = ser.read(2)
    nrbytes = struct.unpack('<h' , nrbytes)[0]
    if nrbytes == 0:
        return []
    datastring = ser.read(nrbytes)
    print nrbytes

    structtuple = struct.unpack('<' + str(nrbytes/2) + 'h' , datastring)
    #print structtuple, type(structtuple), len(structtuple)
    #assert(len(structstring) % 2 == 0)
    retdata = []
    for i in xrange(0,len(structtuple),2):
        retdata.append((structtuple[i],structtuple[i+1]))
    return retdata

if __name__ == '__main__':
    main()
    #print getData(input(),input())
    #time.sleep(3)
    #send(0,2)
    #assert(getData() == [(664,0),(894,1),(673,2),(853,3),(23,3),(212,2),(856,1),(853,0)])
    #send(2,2)
    #assert(getData() == [(664,0),(894,1),(673,2),(853,3),(23,3),(212,2),(856,1),(853,0)])
