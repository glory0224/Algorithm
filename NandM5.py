# 15654번 백준 N&M5

n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))


nums.sort()

seq = []

def dfs():
    if len(seq) == m:
        
        print(' '.join(map(str, seq)))
        return
    
    for i in range(len(nums)):
        if nums[i] not in seq:
            seq.append(nums[i])
            dfs()
            seq.pop()
            
        
dfs()


    