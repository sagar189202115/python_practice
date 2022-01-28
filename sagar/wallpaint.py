l=[0,1,0,3,12]
i=len(l)
zero=l.count(0)
x=0
while True:
    if(x==len(l)-zero):
        break
    print(l[x])
    if l[x]==0:
        print(l)
        l.append(l.pop(l[x]))
    
    x+=1
        
print(l)
