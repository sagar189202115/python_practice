q = int(input().strip())
for q_itr in range(q):
    n = int(input().strip())
    container = []
    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))
    for x in range(0,n):
        sum1=0
        sum2=0
        for y in range(0,n):
            sum1+=container[x][y]
            sum2+=container[y][x]
        if(sum1>sum2):
            print("not possible",q_itr+1)
            break
    
