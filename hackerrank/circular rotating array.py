def circularArrayRotation(a, k, queries):
    # Write your code here
    b=[]
    for i in queries:
        b.append(a[((len(a)-k)+i)%len(a)])
    return b



print(circularArrayRotation([1, 2, 3, 4, 5], 2, [2, 3, 4]))
