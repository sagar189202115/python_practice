a = [1,1,0,1,2,1,0,2]
i = 0
j = 0
k = len(a) - 1
while j <= k:
    if a[j] == 0:
        a[i], a[j] = a[j], a[i]
        i += 1
        j += 1
    elif a[j] == 1:
        j += 1
    else:
        a[j], a[k] = a[k], a[j]

        k -= 1
    print(a)