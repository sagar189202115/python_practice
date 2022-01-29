s = ''
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
st = []
for i in arr:
    if i[0] == '1':
        st.append(s)
        s += i[2:]
    elif i[0] == '2':
        st.append(s)
        rem = int(i[2:])
        s = s[0:len(s) - rem]
    elif i[0] == '3':
        index = int(i[2:]) - 1
        print(s[index])
    elif i[0] == '4':
        s = st.pop()
print(s)
