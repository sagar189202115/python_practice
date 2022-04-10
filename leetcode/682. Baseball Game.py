def baseball(ops):
    res = []
    for i in range(len(ops)):
        if ops[i] == '+':
            res.append(res[-2] + res[-1])

        elif ops[i] == 'C':
            res.pop()
        elif ops[i] == 'D':
            res.append(res[-1] * 2)
        else:
            res.append(int(ops[i]))
    return sum(res)
print(baseball(["5","2","C","D","+"]))