def lettercombination(digits):
    res = []
    if digits == '':
        return []
    d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    def backtrack(idx, temp):
        if idx >= len(digits):
            res.append(''.join(temp))
            return
        for i in d[digits[idx]]:
            temp.append(i)
            backtrack(idx + 1, temp)

            temp.pop()

    backtrack(0, [])
    return res
print(lettercombination('2434'))