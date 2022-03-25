def searchmatrix(matrix,target):
    for i in range(len(matrix[0])):
        high = len(matrix) - 1
        low = 0
        mid = (high + low) // 2

        while low <= high:
            if matrix[mid][i] == target:
                return True
            elif target < matrix[mid][i]:

                high = mid - 1
                mid = (low + high) // 2
                print(high, low)
            else:
                low = mid + 1
                mid = (low + high) // 2
            print(low <= high)
    return False
mat=[]
n=int(input())

for i in range(n):
    mat.append(list(map(int,input().split())))
target=int(input())
print(searchmatrix(mat,target))