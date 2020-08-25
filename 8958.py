n = int(input())

for i in range(0, n):
    a=[]
    b=[]
    total=0
    a = input()
    if a[0]=='O':
        b.append(1)
    elif a[0]=='X':
        b.append(0)
    total+=b[0]
    for j in range(1, len(a)):
        if a[j]=='O':
            if b[j-1]!=0:
                b.append(b[j-1]+1)
            else:
                b.append(1)
        elif a[j]=='X':
            b.append(0)
        total+=b[j]
    print(total)