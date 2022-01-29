m = 5
arr = [1, 2, 3, 2, 3, 4]
for i in range(len(arr)):
    if m - arr[i] in arr[i + 1:]:
        print(i + 1, arr[i + 1:].index(m - arr[i]) + 2 + i)
        break
