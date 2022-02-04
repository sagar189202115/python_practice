contests=[[5 ,1],[2 ,1],[1, 1],[8, 1],[10, 0],[5, 0]]
k=3

su = 0
d = {}
zero=0
s=0
one=0
l=set()
for i in contests:

    if i[1]==1:
        l.add(i[0])
        one+=1
    if i[1]==0:
        su += i[0]
j=sorted(l,reverse=True)
su+=sum(j[:k])-sum(j[k:])

print (su)