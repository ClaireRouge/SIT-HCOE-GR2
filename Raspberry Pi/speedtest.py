import time,math,random

def myfast():
    #random.uniform(0,3.14)
    math.sin(random.uniform(0,1))

n = 100000
t0 = time.clock()
for i in range(n): myfast()
t1 = time.clock()


print t1-t0
