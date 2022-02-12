l = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
# l=[-1]
maxx =[]
s = 0
for i in l:
    s+=i
    maxx.append(max(i,s))
    s=maxx[-1]



print(max(maxx))
