# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:59:31 2021

@author: xalst
"""

a, b = map(int, input().split())

m = list(map(int, input().split()))


start = 0
h = 0
end = max(m)
while start<=end:
    mid=(start+end)//2
    sum1 = 0
    sum1 = sum(i-mid if i > mid else 0 for i in m)
    if b > sum1:
        end = mid -1
    else:
        h = mid
        start = mid + 1

print(h)

