import math

h1=int(input("starting height:"))
h2=0
hf=0
t2=0
t3=0
tf=0
v1=int(input("starting velocity:"))
v2=0
v3=0
a=int(input("acceleration:"))

x=(((v2)*(v2))-((v1)*(v1)))
h2=x/(2*a)
hf=h1+h2

#print hf

t2=(v2-v1)/a

#print t2

v3=-1*((v2*v2)+(2*a*hf))

#print math.sqrt(v3)

t3=-1*(math.sqrt(v3)-v2)/a

#print t3

tf=t3+t2

#print tf

print "The time is "+str(tf)
print "The velocity is "+str(math.sqrt(v3))
print "The max height is "+str(hf)
