a=5
b="prime"
for x in range(2,a):
    if a%x==0:
        b="composite"
else:
    print "the number is "+b
