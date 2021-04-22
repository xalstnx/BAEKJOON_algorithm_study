# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:47:39 2021

@author: xalst
"""
n,m = map(int,input().split())

s = [[0]*n for i in range(n)]
l = [[0]*n for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    s[a-1][b-1] = 1
    l[a-1][b-1] = c

def bfs(start):
    pos_queue = [start]
    cnt_queue = [start]
    k=0
    sum1=0
    while k<n:
        pos = pos_queue.pop(0)
        cnt = cnt_queue.pop(0)
        for i in range(n):
            if pos != start and i == start and s[pos][i] == 1:
                sum1+=l[pos][i]
                return sum1
            if s[pos][i] and i not in cnt_queue:
                cnt_queue.append(i)
                pos_queue.append(i)
                sum1+=l[pos][i]
        k+=1
    return -1

little = 9999999
little_i = 999
for i in range(0, n):
    if(bfs(i) < little and bfs(i)!=-1):
        little = bfs(i)
        little_i = i

print(little)