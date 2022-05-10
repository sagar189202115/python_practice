def conbinations(n,k):
    res = []


    def backtrack(idx=1, r=[], c=0):
        if c == k:
            res.append(r[:])
            return
        for i in range(idx, n + 1):
            r.append(i)
            backtrack(i + 1, r, c + 1)
            r.pop()


    backtrack()
    return res
print(conbinations(4,2))