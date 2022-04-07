def threesumclosest(arr,target):
    x = len(arr)
    arr.sort()
    c = arr[0] + arr[1] + arr[-1]
    i = 0
    j = x
    for k in range(x - 1):
        i = k + 1
        j = x - 1
        while i < j:
            csum = arr[i] + arr[j] + arr[k]
            if csum > target:
                j -= 1
            else:
                i += 1
            if abs(csum - target) < abs(c - target):
                c = csum
    return c
print(threesumclosest([-1,2,1,-4],1))
