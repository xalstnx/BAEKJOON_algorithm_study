a=input()

bigalpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
smallalpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

pos=9999
torf=0
ttorf=0

j=0
for i in bigalpha:
    num[j]+=a.count(i)
    j+=1
j=0
for k in smallalpha:
    num[j]+=a.count(k)
    j+=1


for i in range(0,len(num)):
    if num[i]==max(num):
        if torf==1:
            ttorf=1
            break
        else:
            pos=i
            torf=1
            
if ttorf==1:
    print('?')
else:
    print(bigalpha[pos])