# 백준 1707번 이분 그래프 문제 

# https://ji-gwang.tistory.com/293?category=1044736

# dfs로 문제 풀이 

import sys

input = sys.stdin.readline

# 정점에 해당하는 개수가 최대 20000까지로 문제에서 제시했기 때문에 재귀 깊이 제한을 늘려준다.
sys.setrecursionlimit(20000)

T = int(input())

def dfs(start, group):
    global error
    # 만약 사이클이 true일때 재귀 탈출 
    if error:
        return

    visited[start] = group
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group) # 다른 그룹으로 설정해준다.
        elif visited[start] == visited[i]: # 인접한데 같은 그룹이라면
            error = True # 에러를 True
            return # 그 후 재귀 종료 
            
for _ in range(T):
    # 정점의 개수와 간선의 개수를 map으로 각각 받아준다.
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)] # 빈 그래프를 생성한다.
    
    visited = [False] * (V+1) # 방문한 정점을 체크한다.
    
    # 이분 그래프인지 아닌지 여부 판단용 변수
    error = False
    
    # 각 정점마다 간선 연결 그래프 생성
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
            
    for i in range(1, V+1):
        if not visited[i]: # 방문하지 않았을 경우
            dfs(i, 1) # dfs 탐색
            if error: # 만약 에러가 참이면
                break # 탈출
            
    if error:
        print("NO")
    else:
        print("YES")
                