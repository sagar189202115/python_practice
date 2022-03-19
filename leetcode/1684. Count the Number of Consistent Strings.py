c=0
words=["ad","bd","aaab","baa","badab"]
allowed='abc'
for i in words:
    flag=1
    for j in set(i):
        if j not in allowed:
            flag=0
            break
    if flag:
        c+=1
print(c)