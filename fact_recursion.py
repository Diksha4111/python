#To print the sum of n natural no. using recursion
def sum(n):
    if n<=1:
        return 1
    else:
        return n+sum(n-1)
n=int(input("enter a no.:"))
print("the sum is:",sum(n))
    


