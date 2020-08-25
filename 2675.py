n=int(input())

for i in range(0, n):
    a=input().split()
    b=a[1]
    for j in range(0,len(b)):
        for k in range(0,int(a[0])):
            print(b[j], end='')
    print('')