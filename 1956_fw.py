# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:31:40 2021

@author: xalst
"""

n,m = map(int,input().split())

s = [[99999]*n for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    s[a-1][b-1] = c
    
for k in range(n):
    for i in range(n):
        for j in range(n):
                s[i][j] = min(s[i][j],s[i][k] + s[k][j])


result = 99999
for i in range(n):
    result = min(result, s[i][i])
if result == 99999:
    print(-1)
else:
    print(result)