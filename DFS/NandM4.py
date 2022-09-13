# 15652번 백준 N&M4

n, m = list(map(int, input().split()))

seq= []

def dfs(start):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start, n+1):
        
            seq.append(i)
            dfs(i)
            seq.pop()
            
dfs(1)
