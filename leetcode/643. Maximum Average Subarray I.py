import math


def findMaxAvg(nums,k):
    avg = -math.inf
    t = 0
    j = 0
    for i in range(len(nums)):
        t += nums[i]
        if i >= k - 1:
            te = t / k
            if te > avg:
                avg = te
            t -= nums[j]
            j += 1
    return avg