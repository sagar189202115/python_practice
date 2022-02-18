def cookie():

    k=7
    c=0
    a = list(map(int, input().split()))
    a.sort()
    while len(a)>=2 and a[0]<k:
        r=a.pop(0)
        el=(r+(2*a.pop(0)))
        print(el)
        for i in range(len(a)):
            if el>a[i]:
                continue
            break
        a.insert(i,el)
        c+=1
    return -1 if a[0]<k else c
print(cookie())