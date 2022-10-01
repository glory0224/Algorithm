# 백준 11724번 연결요소 개수 문제 

# bfs 방식으로 풀기 

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 방문 처리 
visited = [False] * (n+1)
# 컴포넌트 그래프 개수 저장용
count = 0 

def bfs(start):
    que = deque([start]) # 큐 자료구조에 시작 노드 넣기 
    visited[start] = True # 방문 처리 
    while que:
        node = que.popleft() # while문을 계속 돌면서 FIFO 방식으로 큐 자료구조 노드 검사, 모두 검사했을 경우 visited가 False로 바뀌면서 while문 종료 
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
        
# 1 ~ n번 노드를 각각 돌면서
for i in range(1, n +1):
    if not visited[i]: # 만약 방문 하지 않았다면 
        if not graph[i]: # 그리고 그래프가 비어있다면
            count += 1 # 개수 + 1
            visited[i] =  True # 방문 처리
        else: # 만약에 그래프가 비어있지 않다면 (어느 점과 연결된 점이 있을 경우)
            bfs(i) # 해당 i를 시작노드로 해서 bfs를 돌아준다.
            count += 1 # 개수 + 1
            
print(count)
            