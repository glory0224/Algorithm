# 백준 1707번 
# bfs 풀이 

import sys

from collections import deque

input = sys.stdin.readline

# BFS
def bfs(start, group):
    queue = deque([start]) # 시작의 정점 값을 큐에 담는다.
    visited[start] = group # 시작 정점 그룹을 설정
    while queue: # 큐가 존재 하면 계속 돈다.
        x = queue.popleft() # 큐의 맨앞 원소를 뺀다. -> while문의 종료 조건

        for i in graph[x]: #해당 정점에서 갈 수 있는 하위 정점들을 돈다.
            if not visited[i]: # 만약의 그 정점들이 아직 방문하지 않았다면
                queue.append(i) # 그 정점들을 추가하고 
                visited[i] = -1 * visited[x] # 상위 정점과 다른 그룹으로 편성한다.
            elif visited[i] == visited[x]: # 만약 정점들을 이미 방문했었는데 같은 그룹이라면
                return False # False를 리턴하고 나온다.
    
    return True # 위의 조건에 걸리지 않았다면 True를 리턴한다.
                
                
# 입력 값을 바로 받아서 for문 
for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [False] * (V+1) # 방문한 정점 체크 
    
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프 
        
    for i in range(1, V+1):
        # 0이 아닌 1과 -1은 모두 true 결국 not true이기 때문에 처음 함수 이외에는 다 if문을 타지 않는다. 따라서 첫번째 예제에서는 'YES' 출력!
        # 내가 착각한 부분 = -1의 값은 false라고 생각했다. 0 이외에는 다 true!!!!! 꼭 기억하자
        if not visited[i]: # 방문한 정점이 아니면, bfs를 수행한다.
        
           result = bfs(i, 1) # 시작과 그룹을 넣어준다. 그룹은 1과 -1로 나눠준다.
           if not result:
               break
           
           
    print('YES' if result else 'NO') 

