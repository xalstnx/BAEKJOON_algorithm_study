n = int(input())

a = list(map(int, input().split()))

mmax = max(a)

total=0

for i in range(len(a)):
    total+=a[i]/mmax*100

total/=n
print(total)