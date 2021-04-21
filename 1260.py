# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:31:31 2021

@author: xalst
"""

n,m,v = map(int,input().split())

s = [[0]*n for i in range(n)]
visit = [0 for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1
    
def dfs(start):
    visit[start] = 1
    print(start+1, end=" ")
    for i in range(n):
        if s[start][i] == 1 and visit[i] == 0:
            dfs(i)
            
dfs(v-1)
print()
def bfs(start):
    pos_queue = [start]
    cnt_queue = [start]
    while len(pos_queue)!=0:
        pos = pos_queue.pop(0)
        print(pos+1, end=" ")
        for i in range(n):
            if s[pos][i] and i not in cnt_queue:
                cnt_queue.append(i)
                pos_queue.append(i)
                
bfs(v-1)