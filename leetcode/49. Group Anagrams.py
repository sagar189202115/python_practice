def anagramslist(strs):
    d = {''.join(sorted(list(map(str, strs[i])))): [] for i in range(len(strs))}
    r = []
    for i in range(len(strs)):
        a = ''.join(sorted(list(map(str, strs[i]))))
        d[a].append(strs[i])
    for k, v in d.items():
        r.append(d[k])
    return r
print(anagramslist(["eat","tea","tan","ate","nat","bat"]))