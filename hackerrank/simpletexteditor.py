s=''
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
st=[]
for i in arr:
    if i[0]=='1':
        
        st.append(s)
        s+=i[2:]
        print(s)
    if i[0]=='2':
        st.append(s)
        rem=int(i[2:])
        s=s[0:len(s)-rem]
        print(s)
    if i[0]=='3':
        inde=int(i[2:])-1
        print(s[inde])
        print(s)
    if i[0]=='4':
        
        s=st.pop()
        print(s)
        
       
    


                       
        
        
