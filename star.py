def star():
    x=int(input("enter any no.:"))
    for a in range(x):
        for b in range(0,a+1):
            print("*",end='')
        print()
star()        
