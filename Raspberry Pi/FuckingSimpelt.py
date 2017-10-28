import FearVR
import math
import serial
import struct
import time
import numpy
#SERIAL STUFF
ser = serial.Serial('/dev/ttyACM0', 115200)

data = []

dir = 0.0
speed = 70

time.sleep(3)

p1 = 0
p2 = 0

def getData():
    nrbytes = ser.read(2)
    nrbytes = struct.unpack('<h' , nrbytes)[0]
    if nrbytes == 0:
        return []
    datastring = ser.read(nrbytes)
    #print nrbytes

    structtuple = struct.unpack('<' + str(nrbytes/2) + 'h' , datastring)
    #print structtuple, type(structtuple), len(structtuple)
    #assert(len(structstring) % 2 == 0)
    retdata = []
    for i in xrange(0,len(structtuple),2):
        retdata.append((structtuple[i],structtuple[i+1]))
    return retdata
	
def send(m1,m2):
    print m1, m2
    ser.write(chr(int(-m1)/2+128) + chr(int(-m2)/2+128))
	
	
send(0,0)
def main():
	global dir
	while (True):
		m1 = speed
		m2 = speed
		getData()
		for i in range(0, len(data)):
			if 40 < data[i][1] < 50:
				p1 = data[i][0]
			elif 130 < data[i][1] < 140:
				p2 = data[i][0]
		dir = (p1 - p2)/100
		if (dir < 0):
			m1*=(1 - abs(dir))
		else:
			m2*=(1 - abs(dir))
		send(m1, m2)
		
try:
	main()
except serial.serialutil.SerialException:
	try:
		print "Connecting again"
		ser
		ser = serial.Serial('/dev/ttyACM0', 115200)
		time.sleep(3)
	except serial.serialutil.SerialException:
		pass