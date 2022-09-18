#6603번 로또

# dfs로 문제 풀기 

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')        
        print()
        return    
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
        
combi = [0 for i in range(13)] # 6개의 인덱스로 조합을 짤 때 최대 수가 0 ~ 13 사이의 수이기 때문에 이렇게 지정
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()


