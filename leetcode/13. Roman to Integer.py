s='XIIIV'
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

j=0
k=d[s[-1]]
su=0
for i in s[::-1]:

    if d[i]<k:
        su-=d[i]
    else:
        su+=d[i]
        k=d[i]
print(su)