x=[]
y=[]

for i in range(10):
    x=x+[range(10)]
    
for i in range(10):
    yy=[]
    for j in range(10):
        yy=yy+[i]

    y=y+[yy]
        
print x
print y
