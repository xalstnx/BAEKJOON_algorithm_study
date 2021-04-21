# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:29:18 2021

@author: xalst
"""

n = int(input())
m = int(input())

s = [[0]*n for i in range(n)]
visit = [0 for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1
    

def dfs(start):
    visit[start] = 1
    for i in range(n):
        if s[start][i] == 1 and visit[i] == 0:
            dfs(i)

k=0
dfs(k)
cnt = 0
for i in range(0,n):
    if i==k:
        continue
    else:
        if visit[i] == 1:
            cnt+=1
print(cnt)