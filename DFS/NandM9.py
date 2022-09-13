# 백준 15663번 N과 M 9

n, m = list(map(int, input().split()))

nums = sorted(list(map(int, input().split())))

visited = [False] * n

seq = []



def dfs(i):
    if len(seq) == m:
        
        print(' '.join(map(str, seq)))
        return
    
    remember_me = 0 
    
    for i in range(n):
        if not visited[i] and nums[i] not in seq:
            visited[i] =True
            seq.append(nums[i])
            remember_me = nums[i]  
            dfs()
            visited[i] =False
            seq.pop()
                
dfs()
