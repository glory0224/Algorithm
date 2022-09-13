# 백준 15656번 N&M7


n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))


nums.sort()

seq = []

def dfs():
    if len(seq) == m:
        
        print(' '.join(map(str, seq)))
        return
    
    for i in range(n):
            seq.append(nums[i])
            dfs()
            seq.pop()
            
dfs()
