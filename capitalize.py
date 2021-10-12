def solve(s):
    l=s.split()
    for i in l:
        cap=i.capitalize()
        s=s.replace(i,cap)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
