import FearThePoints
import math
import serial
import struct
import time
#SERIAL STUFF
ser = serial.Serial('/dev/ttyACM0', 115200)

data = []

def main():
    send(0,0)
    time.sleep(1) #make sure arduino has collected data

    while True:
        newData = getData()
        if newData != []:

            for i in xrange(len(data)-2,0,-1):
                if data[i][1] == newData[-1][1] and data[i-1][1] == newData[-2][1]:
                    data = data[i+1:]
                    break
            else:
                data = []

                data.extend(newData)

        direction = FearThePoints.run(map(lambda x: (x[0],x[1]/180.0*math.pi),data))
        m1 = (128 - int(128*math.sin(direction)))*(1,-1)[math.cos(direction) < 0]
        m2 = (128 - int(-128*math.sin(direction)))*(1,-1)[math.cos(direction) < 0]

        send(m1,m2)

def send(m1,m2):
    ser.write(chr(int(m1)/2+128) + chr(int(m2/2+128)))

def getData():
    nrbytes = ord(ser.read())
    if nrbytes == 0:
        return []
    datastring = ser.read(nrbytes)

    structstring = struct.unpack('<' + str(nrbytes)/2 + 'h' , datastring)
    #assert(len(structstring) % 2 == 0)
    retdata = []
    for i in xrange(0,len(structstring),2):
        retdata.append((structstring[i],structstring[i+1]))
    return retdata

if __name__ == '__main__':
    #main()
    #print getData(input(),input())

    send(0,2)
    assert(getData() == [(3,0),(6,1),(0,2),(6,3),(7,3),(3,2),(2,1),(2,0)])
    send(1,2)
    assert(getData() == [(664,0),(894,1),(673,2),(853,3),(23,3),(212,2),(856,1),(853,0)])
