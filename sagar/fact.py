n=1000
print("hello")
for x in range(5,n+1):
    fact=1
    zero=0
    for i in range(2,x+1):
        fact*=i
    f=fact
    while(f%10==0):
        zero+=1
        f//=10
    print(x," ",zero)
