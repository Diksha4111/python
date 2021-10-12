n = int(input())
student_marks = {}
sum=0
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
c=student_marks[query_name]
for i in c:
    sum+=i
print('%.2f'%(sum/len(c)))
