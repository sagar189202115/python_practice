def cwmw(height):
    i = 0
    j = len(height) - 1
    maxx = 0
    while i < j:
        ma = (abs(j - i)) * min(height[j], height[i])
        if ma > maxx:
            maxx = ma
        if height[i] < height[j]:
            i += 1
        elif height[j] < height[i]:
            j -= 1
        else:
            j -= 1
            i += 1
    return maxx
print(cwmw([6,4,2,5,4,6,1,5]))