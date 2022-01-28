student=[]
for _ in range(int(input())):
    student.append([(input()),float(input())])
student.sort(key= lambda x:x[1])
print(student,len(student))
minn=student[0][1]
student.pop(0)
print(student,len(student))
minn=student[0][1]
for i in range(0,len(student)):
    if (minn==(student[i][1])):
        print(student[i])
