def solution(numbers, target):
    answer = 0
    
    def dfs(idx, now):
        nonlocal answer
        
        if idx == len(numbers)-1:
            if now == target:
                answer += 1
            return
        
        if idx == 0:
            dfs(idx+1,now+numbers[idx+1])
            dfs(idx+1,now-numbers[idx+1])
            dfs(idx+1,-now+numbers[idx+1])
            dfs(idx+1,-now-numbers[idx+1])
        else:
            dfs(idx+1,now+numbers[idx+1])
            dfs(idx+1,now-numbers[idx+1])
    
    dfs(0,numbers[0])
    return answer