# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:28:20 2021

@author: xalst
"""

a = list(map(int, input().split()))

b = list(map(int, input().split()))

start = 0
end = 0
sum1 = 0
n = 0

while start < a[0]:
    while end < a[0] and sum1<a[1]:
        sum1+=b[end]
        end+=1
    
    if(sum1==a[1]):
        n+=1
    sum1-=b[start]
    start+=1
            
print(n)
