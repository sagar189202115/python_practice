num=int(input())
print(2**len(bin(num)[2:])-num-1)