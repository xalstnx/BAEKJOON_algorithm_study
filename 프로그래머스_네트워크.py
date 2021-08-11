def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)]
    
    def dfs(idx):
        nonlocal visit
        nonlocal answer
        visit[idx] = 1
        for j in range(n):
            if computers[idx][j] == 1 and visit[j] == 0:
                dfs(j)
    
    for i in range(n):
        if visit[i] == 0:
            dfs(i)  
            answer+=1
        
    
    return answer