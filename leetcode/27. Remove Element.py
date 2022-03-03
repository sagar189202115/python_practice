from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    c = 0
    while i < len(nums):
        if (nums[i] == val):
            nums.remove(nums[i])
            nums.append('_')
            c += 1
        else:
            i += 1
    return len(nums) - c
nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))