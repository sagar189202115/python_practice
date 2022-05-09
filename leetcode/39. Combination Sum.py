def combinationsum(candidates,target):
    re = list()

    def backtrack(su, r, idx):

        if su == target:
            re.append(r[:])
            return
        if su > target:
            return
        for i in range(idx, len(candidates)):
            r.append(candidates[i])
            backtrack(su + candidates[i], r, i)
            r.pop()

    backtrack(0, [], 0)
    return re
print(combinationsum([2,3,6,7],7))