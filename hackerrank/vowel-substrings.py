s='qwdftr'
k=5
d = {}
v = 0
j = k-1


for i in s[0:j+1]:
    if i in 'aeiou':
        v += 1

i = 0

while j < len(s)-1:



    if s[i-1] in 'aeoiu':
        v -= 1
    if s[j] in 'aeiou':
        v += 1
    if v not in d.values():
        d[s[i:j + 1]] = v
    j += 1
    i += 1
if len(d) == 0:print('Not found!')
print(max(d))