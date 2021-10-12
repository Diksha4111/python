x=set(input().split())
n=int(input())
for i in range(n):
    a=set(input().split())
    if((x==a) or (a.intersection(x)!=a)):
        c='False'
        break
    else:
        c='True'
print(c)

 
