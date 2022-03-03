def climbstairs(n):
    l = [1, 2]
    if n < 3:
        return n
    for i in range(3, n + 1):
        l.append(l[i - 2] + l[i - 3])
    return l[-1]
print(climbstairs(6))