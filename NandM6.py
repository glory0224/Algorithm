# 백준 15655번

n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))


nums.sort()

seq = []

def dfs(start):
    if len(seq) == m:
        
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start, n):
        if nums[i] not in seq:
            seq.append(nums[i])
            dfs(i+1)
            seq.pop()
            
dfs(0)