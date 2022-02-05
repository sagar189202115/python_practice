def getMax(operations):
    st = []
    res = []
    for i in operations:
        if i[0] == '1':
            if st:
                st.append(max(int(i[2:]), st[-1]))
            else:
                st.append(int(i[2:]))

        elif i[0] == '2':
            st.pop()
        elif i[0] == '3':
            res.append(st[-1])
    return res


n = int(input().strip())
ops = []
for _ in range(n):
    ops_item = input()
    ops.append(ops_item)
print(getMax(ops))