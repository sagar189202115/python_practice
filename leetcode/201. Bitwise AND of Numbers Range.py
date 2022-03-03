def rangebitwise(left,right):
    r = left
    if len(bin(left)[2:]) < len(bin(right)[2:]): return 0
    for i in range(left + 1, right + 1):
        r &= i
        if r == 0: return 0
    return r
print(rangebitwise(34,56))