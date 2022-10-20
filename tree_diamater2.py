# 백준 1967번 트리의 지름 문제 
# dfs 두번 이용해서 문제 풀기 

import sys

input = sys.stdin.readline
# dfs 사용할 때 timeout 방지용 
sys.setrecursionlimit(10**9)

n = int(input())

# 입력받고 넣어줄 2차원 그래프 
graph =  [[] for _ in range(n + 1)]

# 트리 구현 
for _ in range(n - 1):
    # 부모, 자식, 가중치 
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# print(graph)

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1: # 방문 체크 
            distance[a] = wei + b # 가중치(여기서는 거리) 증가
            dfs(a, wei + b)

# 1번 노드에서 가장 먼 곳을 찾는다. 
distance = [-1] * (n + 1)  # 방문 여부 확인
distance[1] = 0 # 시작값 초기화
dfs(1, 0)


# 위의 dfs 탐색으로 찾은 노드에 대한 가장 먼 노드를 구한다. 
start = distance.index(max(distance))
# print(start)
distance = [-1] * (n + 1) # 위에서 distance 값이 변경되었기 때문에 다시 초기화 
distance[start] = 0 # 시작값 초기화
dfs(start, 0) # 가장 먼 노드부터 재탐색

print(max(distance))