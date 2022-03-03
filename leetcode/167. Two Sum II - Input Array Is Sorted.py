from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    indices = []
    st = set(numbers)

    for x in st:
        if (target - x in numbers[numbers.index(x) + 1:]):
            indices.append(numbers.index(x) + 1)
            numbers.pop(numbers.index(x))
            indices.append(numbers.index(target - x) + 2)
            break

    return indices
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))