def print_formatted(number):
    ok=len('{:b}'.format(number))
    for i in range (1,number+1):
        print('{0:{a}d} {0:{a}o} {0:{a}X} {0:{a}b}'.format(i,a=ok))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
