a=[4,6,5,3,3,1]
final=[]
k=[]
maxx=0
for i in a:
    maxx=max(a.count(i-1)+a.count(i),maxx)
    maxx=max(a.count(i+1)+a.count(i),maxx)
print(maxx)
