# 15651번 백준 문제 N&M3

n, m = list(map(int, input().split()))

seq = []

def dfs():
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(1, n+1):
        
            seq.append(i)
            dfs()
            seq.pop()
            
dfs()
