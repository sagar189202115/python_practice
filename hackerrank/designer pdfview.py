word='abc'
h=[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
alp = "abcdefghijklmnopqrstuvwxyz"
d = {alp[i]: i for i in range(26)}
idx = 0
for i in word:
    idx = max(idx, h[d[i]])
print(idx * len(word))