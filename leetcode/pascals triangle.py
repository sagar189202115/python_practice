res=[[1]]
for i in range(6):
    t=[1]
    for j in range(0,len(res[-1])-1):
        t.append(res[-1][j]+res[-1][j+1])
    t.append(1)
    res.append(t)
print(res)
