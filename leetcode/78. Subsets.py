nums='sagar'
s = [[]]
for i in nums:
    for j in range(len(s)):
        s.append(s[j] + [i])
print(s)