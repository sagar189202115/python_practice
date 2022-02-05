import numpy
ar=[]
n,m=(map(int,input().split()))
for i in range(n):
    ar.append(list(map(int,input().split())))
my_ar=numpy.array(ar)
print(numpy.prod(numpy.sum(my_ar,axis=0)))