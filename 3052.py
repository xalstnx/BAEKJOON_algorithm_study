i = 0

count=0

a=[]

while i<10:
    ans = int(input())%42
    if a.count(ans)==0:
        count+=1
    a.append(ans)
    print(a)
    i+=1
    
print(count)