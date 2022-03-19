import math
def longestCommonPrefix(strs):
    res=''
    flag=0
    mini=math.inf
    for i in strs:
        mini=min(mini,len(i))
    for i in range(mini):
        t=strs[0][i]
        for j in range(1,len(strs)):
            if not(t==strs[j][i]):
                
                flag=1
                break
        
        if flag:
            break
        else:
            res+=t
    return res
print(longestCommonPrefix(["dog","racecar","car"]))
