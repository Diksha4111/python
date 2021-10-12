def print_rangoli(size):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    pattern=alphabet[0:size]
    for i in range(0,size-1,1):
        c=abs(i)
        k=pattern[size:c+1:-1]+pattern[c+1:size]
        print("--"*(c+1)+'-'.join(k)+"--"*(c+1))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
