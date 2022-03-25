def searchmatrix(matrix,target):
    def binarysearch(a):
        high=len(a)-1
        low=0
        mid=(high+low)//2
        while low <=high:
            if a[mid]==target:
                return True
            elif target <a[mid]:
                high=mid-1
                mid=(low+high)//2
            else:
                low=mid+1
                mid=(low+high)//2
        return False
    for i in range(len(matrix)):
        if binarysearch(matrix[i]):
            return True
    return False
mat=[]
n=int(input())

for i in range(n):
    mat.append(list(map(int,input().split())))
target=int(input())
print(searchmatrix(mat,target))