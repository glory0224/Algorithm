# 백준 1939번 중량제한 문제 

# https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-1939%EB%B2%88-%EC%A4%91%EB%9F%89%EC%A0%9C%ED%95%9C-1-Python

# 문제 아이디어

# 최소와 최대 중량을 정한 다음 mid를 통해 중간 값을 계산해서
# BFS를 통해 목적지까지 도달할 수 있을까 살펴본 다음에 mid 값을 이진탐색으로 조절하며 답을 찾는다. 

# BFS + 이진 탐색을 활용한 문제 


from collections import deque
import sys

input = sys.stdin.readline

def bfs(mid):
    visited[start] = 1 # 방문 표시
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        # print("now : " + str(now))
        if now == end:
            return True
        for nx, nc in graph[now]:
            # print("nx : " + str(nx))
            # print("nc : " + str(nc))
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1
    
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # print(graph)
    for i in range(1, n + 1):
        graph[i].sort(reverse=True) # 최고 무게순으로 정렬

    # print(graph)

    start , end = map(int, input().split())
    low, high = 1, 1000000000
    while low <= high:
        visited = [0 for _ in range(n + 1)] # 각 섬의 방문 여부
        # print("low : " + str(low))
        # print("high : " + str(high)) 
        mid = (low + high) // 2
        # print("mid : " + str(mid))
        if bfs(mid): # 목적지까지 도달이 가능하다면 low를 올린다.
            low = mid + 1
            # print("test")
        else: # 목적지까지 불가능하다면 high를 내린다. 
            high = mid - 1
    
    print(high)

