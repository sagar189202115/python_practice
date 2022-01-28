student=[]
for _ in range(int(input())):
    student.append([(input()),float(input())])
student.sort(key= lambda x:x[1])
minn=student[0][1]
student.pop(0)
if minn==(student[0][1]):
    student.pop(0)
minn=student[0][1]
for i in (0,len(student)):
    if (minn==(student[0][1])):
        print(student[i][0])