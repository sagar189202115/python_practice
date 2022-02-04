i=20
j=23
k=6
c = 0
for a in range(i, j + 1):
    if abs(a - int(str(a)[::-1])) / k == abs(a - int(str(a)[::-1])) // k:
        c += 1
print(c)
