def get_fact(m):
    t = 0
    while m:
        r = m // 5
        t = t + r
        m = r
    return t


n = int(input())
print(get_fact(n))
