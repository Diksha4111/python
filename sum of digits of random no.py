#to calculate the sum of all the digits of any three digit random no.
import random
x=random.random()*900+100
x=int(x)
print(x)
sum=0
a=x//100
b=(x//10)%10
c=x%10
sum=a+b+c
print(sum)
