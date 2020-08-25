c = int(input())

for i in range(0,c):
    a=[]
    sum=0
    largenum=0
    percent=0
    a=list(map(int, input().split()))
    for j in range(1,len(a)):
        sum+=a[j]
    sum/=a[0]
    for k in range(1,len(a)):
        if sum<a[k]:
            largenum+=1
    percent = largenum/a[0] * 100
    print('%5.3f%%' %percent)