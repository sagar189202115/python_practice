def goodland(k,arr):
    h = (k * 2) - 1
    c = 0
    i = 0
    while i < len(arr):
        print(i,arr[i-k-1])
        if arr[i] == 0:
            if (i+k-1)<len(arr) and  arr[i + k - 1] == 1:
                c += 1
                i = i + h
                continue
            elif (i-k+1)<len(arr) and arr[i-k+1]==1:
                c+=1
                i+=1
                continue
            else:
                return -1
        i += 1
    return c

print(goodland(2,[0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1]))