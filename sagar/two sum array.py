numbers=[5,25,75]
indices=[]
target=100
for x in range(len(numbers)):
    for y in range(x,len(numbers)-1):
        if(numbers[x]+numbers[y]==target):
            incides.append(x+1)
            incides.append(y+1)
print(indices)
