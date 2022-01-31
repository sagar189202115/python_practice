s = input()
vowels = ['A', 'E', 'I', 'O', 'U']

kevin=0
stuart=0
for i in range(len(s)):
    e=len(s)-i
    if s[i] in vowels:
        kevin+=e
    else:
        stuart+=e

if kevin > stuart:
    print("Kevin ", kevin)
elif stuart > kevin:
    print("Stuart ", stuart)
else:
    print("Draw")
