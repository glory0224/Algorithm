# 백준 15657번 N&M8


n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))


nums.sort()

seq = []

def dfs(start):
    if len(seq) == m:
        
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start, n):
            seq.append(nums[i])
            dfs(i)
            seq.pop()
            
dfs(0)
