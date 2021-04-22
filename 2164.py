# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:20:54 2021

@author: xalst
"""

from collections import deque

n = int(input())

a = deque()

for i in range(n):
    a.append(i+1)
    
while len(a) > 1:
    a.popleft()
    a.append(a.popleft())

print(a[0])