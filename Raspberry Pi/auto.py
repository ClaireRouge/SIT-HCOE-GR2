import FearThePoints
import math
import serial
import struct
import time
#SERIAL STUFF
ser = serial.Serial('/dev/ttyACM0', 115200)

data = []
def main():
    send(128,128)
    time.sleep(1) #make sure arduino has collected data

    while True:
        newData = getData()

        for i in xrange(len(data)-2,0,-1):
            if data[i][1] == newData[-1][1] and data[i-1][1] == newData[-2][1]:
                break
        data = data[i+1:]

        data.extend(newData)
        direction = FearThePoints.run(map(lambda x: (x[0],x[1]/180.0*math.pi),data))
        m1 = (128 - int(128*math.sin(direction)))*(1,-1)[math.cos(direction) < 0]
        m2 = (128 - int(-128*math.sin(direction)))*(1,-1)[math.cos(direction) < 0]

        send(m1,m2)

def send(m1,m2):
    ser.write(chr(int(m1)/2+128) + chr(int(m2/2+128)))

def getData():
    nrbytes = ord(serial.read())
    datastring = serial.read(nrbytes)

    structstring = struct.unpack('<' + str(nrbytes) + 'h' , instr)
    assert(len(structstring) % 2 == 0)
    retdata = []
    for i in xrange(0,len(structstring),2):
        retdata.append((structstring[i],structstring[i+1]))
    return retdata

if __name__ == '__main__':
    main()
    #print getData(input(),input())
