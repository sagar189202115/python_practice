a='aaaabbaa'
maxx=''
i=0
ps=[]
while i<len(a):
    s=''
    for j in range(i,len(a)):
        s+=a[j]
        if s==s[::-1]:
            ps.append(s)
            if len(s)>len(maxx):
                maxx=s

    i+=1
print(maxx)