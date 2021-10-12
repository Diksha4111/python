def minion_game(string):
    s=0
    k=0
    a=['A','E','I','O','U']
    for i in range(len(string)):
        if string[i] in a:
            k+=len(string)-i
        else:
            s+=len(string)-i
        
    if k>s:
        print('Kevin',k)
    elif(s>k):
        print('Stuart',s)
    else:
        print('Draw')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
