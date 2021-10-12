#To print fibonacci series using recursion
def fib_series(x):
    if x<=1:
        return x
    else:
        return(fib_series(x-1)+fib_series(x-2))
x=int(input("enter a no.:"))
print("fibonacci series is:")
for i in range(x):
    print(fib_series(i))






