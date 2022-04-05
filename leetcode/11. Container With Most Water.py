# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the
# ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
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