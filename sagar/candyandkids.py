def solve(n,ar):
    print(sum(ar)%n[1])
a=int(input())
for i in range(a):
    n=list(map(int,input().split()))
    ar=list(map(int,input().split()))
    solve(n,ar)