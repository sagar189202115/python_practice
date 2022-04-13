def anagramslist(strs):
    ar = [''.join(sorted(list(map(str, strs[i])))) for i in range(len(strs))]
    d = {i: [] for i in ar}
    r = []
    for i in range(len(strs)):
        d[ar[i]].append(strs[i])
    for k, v in d.items():
        r.append(d[k])
    return r
print(anagramslist(["eat","tea","tan","ate","nat","bat"]))