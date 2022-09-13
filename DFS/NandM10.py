# 백준 15664번 N&M10

n, m = list(map(int, input().split()))

nums = sorted(list(map(int, input().split())))

check = [False]*n

seq = [ ]


def dfs(start):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    remember_num = 0
    for i in range(start,n):
        if not check[i] and remember_num != nums[i]:
            check[i] = True
            seq.append(nums[i])
            remember_num = nums[i]
            dfs(i+1)
            check[i] = False
            seq.pop()
            
        
dfs(0)
                
        
