def rMCM(arr1, i, j):
    if i == j:
        return 0
    minimum = 100000
    for k in range(i, j):
        count = rMCM(arr1, i, k) + rMCM(arr1, k + 1, j) + arr1[i - 1] * arr1[k] * arr1[j]
        if count < minimum:
            minimum = count
        return minimum


def mcm(arr1, n):
    return rMCM(arr1, 1, n - 1)


arr = [2, 3, 4, 3, 5]
ans = mcm(arr, 5)
print(ans)
