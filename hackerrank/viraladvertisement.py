n=5
c=0
for i in range(9):
    n=(n//2)
    c+=n
    n*=3
    m=c
print(c)