nums=[4,1,2,1,2]
st = {}
for i in nums:
    if i == st[1]:
        st[1] = i
    else:
        st[2] = i
print(st[1])