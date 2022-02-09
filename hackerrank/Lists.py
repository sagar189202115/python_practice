N = int(input())
l = []
arr = []
for i in range(N):
    t = input()
    l.append([t])

for i in l:
    if i[0].split()[0]=='insert':
        if len(arr)==0:

            arr.append(int(i[0].split()[2]))

        else:

            arr.insert(int(i[0].split()[1]), int(i[0].split()[2]))
    elif i[0].split()[0]=='print':
        print(arr)
    elif i[0].split()[0]=='remove':
        arr.remove(int(i[0].split()[1]))

    elif i[0].split()[0]=='append':
        arr.append(int(i[0].split()[1]))
    elif i[0].split()[0]=='sort':
        arr.sort()
    elif i[0].split()[0]=='pop':
        arr.pop()
    elif i[0].split()[0]=='reverse':
        arr = arr[::-1]