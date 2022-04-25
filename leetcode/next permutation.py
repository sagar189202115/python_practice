a = [1,2,3]
permu = []
def backtrack(i, arr, perm):
    if i == len(arr) - 1:

        permu.append(arr[:])
        
    else:
        arr[i-1], arr[0] = arr[0], arr[i-1]
        backtrack(i + 1, arr, perm)
        arr[i-1], arr[0] = arr[0], arr[i-1]


backtrack(-1, a, [])
print(permu)
