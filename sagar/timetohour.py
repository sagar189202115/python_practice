time='10:17:45PM'
n=int(time[0]+time[1])
newtime=""
if(time[-2]=='P' and n<12):
    newtime=str(n+12)+time[-8:-2]
elif(time[-2]=='A' and n>11):
    newtime='00'+time[-8:-2]
else:
    newtime=time[-11:-2]
print(newtime)
