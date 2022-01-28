def getBaseTen(binaryVal):
    count = 0

	#reverse the string
    

    #go through the list and get the value of all 1's
    for i in range(0, len(binaryVal)):
        if(binaryVal[i]):
            count += 2**i
    temp=count
    c=0
    base6=[]
    i=1
    while temp>0:
        base6.append(temp%6)
        #rem=(temp%6)*i
        #i*=10
        #c+=rem
        temp=temp//6
    
    return base6
s=getBaseTen([False,True,True,True,True])
print(s)
