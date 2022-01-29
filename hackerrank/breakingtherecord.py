arr = list(map(int, input().split()))
maxx = minn = arr[0]
maxc = minc = 0
for i in arr:
    if i > maxx:
        maxx = i
        maxc += 1
    if i < minn:
        minn = i
        minc += 1
print(maxc,maxx, minc,minn)
