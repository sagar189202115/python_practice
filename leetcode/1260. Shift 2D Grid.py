def gridshift(grid,o):
    h = len(grid) * len(grid[0])

    k = o % h
    if k == 0:
        return grid
    r = []
    b = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if b >= k:
                b = 0
            if len(r) < k:
                r.append(grid[i][j])
            else:

                r[b], grid[i][j] = grid[i][j], r[b]

            b += 1
    flag = 0
    o = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if b >= k:
                b = 0
            if o >= k:
                flag = 1
                break
            else:
                grid[i][j] = r[b]
                o += 1
                b += 1
        if flag:
            break
    print(r)
    return grid
print(gridshift([[1,2,3],[4,5,6],[7,8,9]],7))