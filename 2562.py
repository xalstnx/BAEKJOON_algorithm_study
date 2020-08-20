a = []

i=0

max1 = 0

maxi = 0

while i<9:
    b = int(input())
    a.append(b)
    if max1 < b:
        maxi = i
        max1 = b
    i+=1

print(max1)
print(maxi+1)