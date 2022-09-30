# 백준 1260번 DFS와 BFS

# 이전에 풀었던 ABCDE 문제와 풀이 방식이 비슷하다.


from sys import stdin

# bfs를 구현하기 위해서는 파이썬에서 deque를 사용해야 시간복잡도를 줄일 수 있다. 
from collections import deque

input = stdin.readline

# 정점 개수, 간선 개수, 시작할 정점 번호 입력 받기
n, m, start = map(int, input().split())
visited = [False] * (n+1)

# 사용할 그래프 2차원 배열 생성 
graph = [[] for _ in range(n+1)]

# 정점과 인접한 간선을 정점과 연결하는 과정
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print("정렬하기 전 : " , graph)

# 작은 노드부터 방문을 시작해야하기 때문에 그래프를 정렬해준다.
for i in range(len(graph)):
    graph[i].sort()
    
# print("정렬하고 난 후 : " , graph)



# dfs 구현 
def dfs(start):
    # 공백을 주면서 start 값 출력
    print(start, end= ' ')
    # 해당 정점 방문
    visited[start] = True
    
    # 배열로 만들어놓은 인접노드를 탐색한다.
    for i in graph[start]:
        if not visited[i]:
            # 시작 정점의 간선에 해당 값을 start로 받아서 깊이 탐색 방식으로 확인한다.
            dfs(i)          
            visited[i] = True

        
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i) # 방문하지 않은 인접 정점의 해당 간선을 모두 큐에 넣고 너비 탐색 방식으로 확인한다. 
                visited[i] = True
                
dfs(start)

# dfs와 bfs를 각자 실행해야 하기 때문에 이미 적용된 visited가 공유되지 않도록 초기화해준다.
visited = [False]*(n+1)
 
print() # 답 형식에 맞춰 개행 

bfs(start)   

