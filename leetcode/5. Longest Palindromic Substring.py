a='abbadabd'
maxx=0
i=0
st=''
m=0
mat=[[True]*len(a) for i in range(len(a))]
for i in range(1,len(a)):
    k=i
    for j in range(len(a)-i):
        #if first and last character is same check previous diognal for true
        if a[j]==a[k]:
            #if prev diagnol is true and len of current palindorme is greater or not
            if mat[j+1][k-1] and m<len(a[j:k+1]):
                mat[j][k]=True
                m=len(a[j:k+1])
                st=a[j:k+1]
            else:mat[j][k]=False

        else:mat[j][k]=False

        k+=1
print(st)