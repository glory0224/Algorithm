# 백준 15665번 N&M12

n, m = list(map(int, input().split()))

nums = sorted(list(map(int, input().split())))

# 1 1 7 7 9 9 같은 수도 허용하기 위해서 False로 체크하지 않는다. 
#check = [False]*n

seq = [ ]


def dfs(start):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    remember_num = 0
    for i in range(start, n):
        if  remember_num != nums[i]:
            seq.append(nums[i])
            remember_num = nums[i]
            dfs(i)
            
            seq.pop()
            
        
dfs(0)
                
        
