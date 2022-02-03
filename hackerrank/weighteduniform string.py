a = 'aaabbbbcccddd'

q = [9, 7, 8, 12, 5]

ans = []
s1 = set()
i = 0
j = 0
su = 0
while i < len(a):
    if a[j] == a[i]:
        su += ord(a[i]) - 96
        s1.add(su)
        i += 1
    else:
        su = ord(a[i]) - 96
        s1.add(su)
        j = i
        i += 1
s2=(set.intersection(s1, q))
for i in q:
    if i in s2:
        ans.append('Yes')
    else:
        ans.append('No')
print(ans)
