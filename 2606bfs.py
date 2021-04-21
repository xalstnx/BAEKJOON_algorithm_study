# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:06:33 2021

@author: xalst
"""

n = int(input())
m = int(input())

s = [[0]*n for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1

    
def bfs(start):
    pos_queue = [start]
    cnt_queue = [start]
    while len(pos_queue)!=0:
        pos = pos_queue.pop(0)
        for i in range(n):
            if s[pos][i] and i not in cnt_queue:
                cnt_queue.append(i)
                pos_queue.append(i)
    return len(cnt_queue)-1

print(bfs(0))
            