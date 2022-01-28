class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        num1=0
        num2=0
        for i in range(1,len(a)+1):
            num1+=int(a[-i])*(2**(i-1))
        for i in range(1,len(b)+1):
            num1+=int(b[-i])*(2**(i-1))
        num3=num1+num2
        binary=""
        
        while(num3>0):
            r=""+str(num3%2)
            binary=r+binary
            num3=num3//2
        if binary=="":
            return "0"
        
        return binary
c1=Solution()

print(c1.addBinary("100110","10101"))
