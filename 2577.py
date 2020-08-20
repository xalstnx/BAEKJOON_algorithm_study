a = input()

b = input()

c = input()

d = str(int(a) * int(b) * int(c))

tt = []

for i in range(len(d)):
    tt.append(d[i])
    
k=0

while k<10:
    cc = d.count(str(k))
    print(cc)
    k+=1