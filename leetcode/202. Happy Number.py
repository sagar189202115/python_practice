def happynumber(n):
    d = set()
    while True:
        s = sum(int(x) ** 2 for x in str(n))
        if s == 1: return True
        if s in d: return False
        d.add(s)
        n = s
print(happynumber(9))