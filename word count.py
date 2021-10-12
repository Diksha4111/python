s='BANANA'
l=s.split()
vowels=['A','E','I','O','U']
kevin=[]
stuart=[]
opk=[]
ops=[]
dk={}
ds={}
s=0
k=0
for j in l:
    for k in range(len(j)):
        if j[k] in vowels:
            kevin.append(j[k:len(j)])
        else:
            stuart.append(j[k:len(j)])
            
for i in kevin:
    for j in range(len(i)):
        for k in range(len(i)-j):
            if i[j] in vowels:
                opk.append(i[j:k])             

final_K=kevin+opk
for i in final_K:
    if i!='':
        dk[i]=final_K.count(i)

for i in dk:
    k+=dk[i]
    print(i,dk[i])
    

for i in stuart:
    for j in range(len(i)):
        for k in range(len(i)-j):
            if i[j] not in vowels:
                ops.append(i[j:k])

final_S=stuart+ops
for i in final_S:
    if i!='':
        ds[i]=final_S.count(i)

for i in ds:
    s+=ds[i]
    print(i,ds[i])




