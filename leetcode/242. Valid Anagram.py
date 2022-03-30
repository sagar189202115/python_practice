def anagram(s,t):
    if len(s) != len(t): return False
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = s.count(s[i])
            if d[s[i]] != t.count(s[i]):
                return False
    return True
print(anagram('anagram','nagaram'))