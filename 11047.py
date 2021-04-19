# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:38:30 2021

@author: xalst
"""

a = list(map(int, input().split()))
b = []
sum = 0
for i in range(a[0]):
    b.append(int(input()))
    
for i in range(a[0]-1, -1, -1):
    if a[1]//b[i] >= 1:
        sum+=(a[1]//b[i])
        a[1]=a[1]%b[i]
        
print(sum)