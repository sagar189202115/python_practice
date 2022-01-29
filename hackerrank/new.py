a=[5,4,3,1]
maxindex=a.index(max(a))
minindex=a.index(min(a))
a[0],a[minindex]=a[minindex],a[0]
a[1],a[maxindex]=a[maxindex],a[1]
print(a)