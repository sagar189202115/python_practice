x1=int(input())
v1=int(input())
x2=int(input())
v2=int(input())
diffdiff=abs(abs((x1+v1)-(x2+v2))-abs(x1-x2))

if(not(diffdiff==0) and abs(x1-x2)%diffdiff==0):
    
    if(abs(x1-x2)>abs((x1+v1)-(x2+v2))):
        print("YES")

else:print("NO")
