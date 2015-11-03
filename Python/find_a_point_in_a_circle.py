import random
#p is the number of random points
p=10000
#n is the number of points in the circle
n=0.

for i in range(p):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (x*x+y*y)<1:
            n=n+1

pi=4*n/p
print pi
