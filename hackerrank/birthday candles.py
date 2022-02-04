l=[3,1,2,3]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
maxx=0
for i in d.keys():
    if maxx<i:
        maxx=i
print(d[maxx])