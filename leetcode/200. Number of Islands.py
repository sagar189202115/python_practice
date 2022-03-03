grid = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
res = 0


def solve(i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return 0
    else:
        grid[i][j] = '-1'
        return 1 + solve(i - 1, j) + solve(i, j - 1) + solve(i, j + 1) + solve(i + 1, j)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1':
            solve(i, j)
            res += 1

print(res)