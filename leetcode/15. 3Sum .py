def threeSum(arr):
    x = len(arr) - 1
    arr.sort()
    c = []
    i = 0
    j = x
    for k in range(len(arr) - 1):
        i = k + 1
        j = x
        while i < j:
            t = arr[i] + arr[j] + arr[k]
            if t == 0:
                if [arr[i], arr[j], arr[k]] not in c:
                    c.append([arr[i], arr[j], arr[k]])
                i += 1
                j -= 1
            elif t < 0:
                i += 1
            else:
                j -= 1

    return c
print(threeSum([-1,0,1,2,-1,-4]))