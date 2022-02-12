s='baab'
l1=list(map(str,s))
i=0
while i<len(l1)-1:
    if l1[i]==l1[i+1]:
        l1.pop(i+1)
        l1.pop(i)
        i-=1
    else:
        i+=1
l=''.join(l1)

print(l)