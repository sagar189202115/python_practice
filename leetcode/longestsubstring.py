s="kwwpwk"


maxx=0
for j in range(0,len(s)):
    t=""
    b=s[j]
    t+=b
    for i in range(j+1,len(s)):
        if(s[i] not in t):
            t+=s[i]
            b=s[i]
        else:
            break
    maxx=max(len(t),maxx)
print(maxx)
