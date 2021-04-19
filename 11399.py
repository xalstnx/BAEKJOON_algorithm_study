# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:38:51 2021

@author: xalst
"""


n = int(input())

a = map(int,input().split())

b = list(a)

c = sorted(b)

sum = 0

for i in range(len(c)):
    for j in range(i+1):
        sum+=c[j]
    print(sum)
        
print(sum)