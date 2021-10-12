n=int(input())
a=input().split()
k=[]
c=set(a)
c1=list(c)
c1.sort()
for i in c1:
    x=int(i)
    k.append(x)
M=max(k)
k.remove(M)
print(int(max(k)))
