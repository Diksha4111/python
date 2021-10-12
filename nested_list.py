students=[]
marks=[]
sec_low=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    x=[name,score]
    students.append(x)
#print(students)
for i in students:
    k=i[1]
    marks.append(k)

c=set(marks)
#print(c)
c1=list(c)
#print(c1)
m=min(c1)
#print(m)
for i in students:
    if(i[1]==m):
        students.remove(i)
c1.remove(m)
m=min(c1)
#print(c1)
#print(students)

for i in students:
    if(i[1]==m):
        sec_low.append(i[0]) 
sec_low.sort()
for i in sec_low:
    print(i)
    
