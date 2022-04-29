def nearbyduplicates(nums,k):
    d = {nums[i]: 0 for i in range(len(nums))}
    l = 0
    for i in range(len(nums)):
        if d[nums[i]] > 0:
            return True
        d[nums[i]] += 1
        if i >= k:
            d[nums[l]] -= 1
            l += 1
    return False