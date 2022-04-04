def subarraydivision(s,d,m):
    i = 0
    t = 0
    c = 0
    for j in range(len(s)):
        t += s[j]
        if j >= m - 1:

            if t == d:
                c += 1
            t -= s[i]
            i += 1
        j += 1
    return c
print(subarraydivision([1,2,1,3,2],3,2))