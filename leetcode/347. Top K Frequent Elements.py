import heapq


def topKFrequent(nums, k):
    nums.sort()

    r = []
    d = {}
    res = []
    heapq.heapify(r)
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1
    for l, v in d.items():
        heapq.heappush(r, [v, l])
        heapq.heappop(r) if len(r) > k else None

    for i in range(len(r)):
        res.append(r[i][1])
    return res
print(topKFrequent([1,1,1,2,2,3],2))