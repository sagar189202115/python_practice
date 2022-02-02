arr = []
for i in range(3):
    a = list(map(int, input().split()))
    arr.append(a)
o = [[1 for i in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        if arr[i][j] % 2 == 1:
            o[i][j] = 1 - o[i][j]
            if i+1 < 3:
                o[i + 1][j] = 1 - o[i + 1][j]
            if j+1 < 3:
                o[i][j + 1] = 1 - o[i][j + 1]
            if i-1 > -1:
                o[i - 1][j] = 1 - o[i - 1][j]
            if j-1 > -1:
                o[i][j - 1] = 1 - o[i][j - 1]

print(o)
