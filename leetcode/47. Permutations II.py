a = [1, 1, 2]
permu = []


def backtrack(i, arr, perm):
    if i == len(arr) - 1 and arr[:] not in permu:

        permu.append(arr[:])
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            backtrack(i + 1, arr, perm)
            arr[i], arr[j] = arr[j], arr[i]


backtrack(0, a, [])
print(permu)
