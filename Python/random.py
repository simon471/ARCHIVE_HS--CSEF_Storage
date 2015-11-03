import random
a=[]
s=0.0

for i in range(20):
    a=a+[random.uniform(0.0,100.0)] 
print a

for h in range(len(a)):
    s=s+a[h]

s=s/len(a)
print s
