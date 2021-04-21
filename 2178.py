# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:07:37 2021

@author: xalst
"""

n,m = map(int,input().split())

pos_queue = [(0,0)]
cnt_queue = [1]

maze = []
for i in range(n):
    maze.append(list(map(int, list(input()))))

def isgo(x,y):
    if 0<=x<n and 0<=y<m:
        if maze[x][y] == 1:
            return True
        else:
            return False
    return False

while len(pos_queue)!=0:
    pos = pos_queue.pop(0)
    cnt = cnt_queue.pop(0)
    
    x = pos[0]
    y = pos[1]
    
    if(pos == (n-1,m-1)):
        print(cnt)        
        break
    elif(maze[x][y] == 0):
        continue
    
    maze[x][y] = 0
    
    if(isgo(x+1,y)):
        pos_queue.append((x+1,y))
        cnt_queue.append(cnt+1)
    if(isgo(x-1,y)):
        pos_queue.append((x-1,y))
        cnt_queue.append(cnt+1)
    if(isgo(x,y+1)):
        pos_queue.append((x,y+1))
        cnt_queue.append(cnt+1)
    if(isgo(x,y-1)):
        pos_queue.append((x,y-1))
        cnt_queue.append(cnt+1)
    