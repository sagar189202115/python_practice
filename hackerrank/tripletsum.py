n = int(input())
arr = [int(input()) for i in range(0, n)]
arr.sort()
print(arr)
triplets = []
for i in range(0, n - 1):
    for y in range(i+1, n):
        if arr[i] + arr[y] in arr:
            triplets.append([arr[i], arr[y], arr[i] + arr[y]])
print(triplets)
