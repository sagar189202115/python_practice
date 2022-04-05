word='abas'
c = 0
t = len(word)
for i in range(t):
    if word[i] in 'aeiou':
        c += (i + 1) * (t - i)
print(c)