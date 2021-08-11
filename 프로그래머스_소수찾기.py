import itertools

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def solution(numbers):
    answer = 0
    n = []
    for i in range(len(numbers)):
        n.append(numbers[i])
    nn = []
    for i in range(1, len(numbers)+1):
        nn+=list(map(''.join, itertools.permutations(n, i)))
    nnn = []
    for i in range(len(nn)):
        nnn.append(int(nn[i]))
    nnn=list(set(nnn))
    
    for i in range(len(nnn)):
        if isPrime(nnn[i]) == True:
            answer+=1
    return answer