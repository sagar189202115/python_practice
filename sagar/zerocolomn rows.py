mat=[]
d={}
for i in range(4):
    t=list(map(int,input().split()))
    mat.append(t)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]==0:
            d[i]=j
for i in range(len(mat)):

    for j in range(len(mat[i])):
        if i in d.keys() or j in d.values():
            mat[i][j]=0
for i in mat:
    print(i)
