# 백준 11724번 연결 요소의 개수 

#첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

import sys

# 
# 파이썬의 기본 재귀 깊이 제한이 1000이기 때문에 재귀로 문제를 푼다면 아래와 같이 setrecursionlimit 메소드로 제한을 늘려주어야 한다. 
# 열심히 풀었는데 이 한줄 때문에 틀리면 자괴감에 빠질 수 있기에.. 파이썬 재귀를 이용한다면 필수적으로 사용하자.
# https://fuzzysound.github.io/sys-setrecursionlimit 참고
sys.setrecursionlimit(5000) 


input = sys.stdin.readline

n, m = map(int, input().split())

cnt = 0

visited = [False] * (1+n)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# dfs 방식으로 해당 그래프를 탐색한다.
def dfs(start, depth):
    
    #해당 노드 방문 체크 한다.
    visited[start] = True
    
    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를 탐색한다.
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)


# 1 ~ n번의 노드를 for문으로 돈다.
for i in range(1, n+1):
    if not visited[i]: # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]: # 그리고 만약 해당 정점에 연결된 그래프가 없다면
            cnt += 1 # 개수를 + 1
            visited[i] = True # 방문 처리 
        else: # 연결된 그래프가 있다면
            dfs(i, 0) # dfs 탐색을 돌아준다.
            cnt += 1 # 개수를 +1
            
print(cnt)            
            
