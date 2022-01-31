a = [2, 6]
b = [24, 36]
m = []
for i in sorted(a, reverse=True):
    v = 1
    c = 1
    st = set()
    while True:
        v = c * i
        st.add(v)
        c += 1
        if v >= min(b):
            break

    m.append(st)
inter = list(set.intersection(*m))
count = 0
for i in inter:
    flag = 0
    for j in b:

        if j % i != 0:
            flag = 1
            break
    if flag == 0:
        count += 1
print(count)
