grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
r = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]==1:
            c = 4
            if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                c -= 1
            if j > 0 and grid[i][j - 1]:
                c -= 1
            if i > 0 and grid[i - 1][j]:
                c -= 1
            if i < len(grid) - 1 and grid[i + 1][j]:
                c -= 1
            r += c
print(r)