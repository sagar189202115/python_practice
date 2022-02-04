arr=[1,4,4,4,3,5,2]
d = {}
for i in range(len(arr)):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
print(d)
di={}
maxx=max(d.values())


for k, v in d.items():
    if maxx==v:
        di[k]=v
print(min(di))

