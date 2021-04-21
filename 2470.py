# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:54:31 2021

@author: xalst
"""

n = int(input())

a = list(map(int,input().split()))
b = sorted(a)

sum1=0

left = 0
right = n-1

little_left = 0
little_right = n-1
little = 9999999999

while left<right:
    sum1 = b[left] + b[right]
    if abs(sum1) < abs(little):
        little = sum1
        little_left = left
        little_right = right
    
    if sum1 >= 0:
        right -= 1
    else:
        left += 1
    
print(b[little_left], b[little_right])
