a=[1,2,4,9,3,7,8,10]
lis=[1 for i in range(len(a))]

for i in range(len(a)):
    maxx=0
    sum=0
    for j in range(i):
        if a[i]>a[j] and lis[j]>maxx:
            maxx=lis[i]
        lis[i]=maxx+1
print(lis)
#longest decreasing sequence
'''print(max(lis))
lis=[1 for i in range(len(a))]
for i in range(len(a)-1,-1,-1):
    maxx=0
    for j in range(i-1,-1,-1):
        if a[i]>a[j] and lis[j]>maxx:
            maxx=lis[i]
        lis[i]=maxx+1

print(max(lis))'''
