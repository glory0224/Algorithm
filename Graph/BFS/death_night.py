
from collections import deque

import sys

input = sys.stdin.readline

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in deathNight:
            ny, nx = y+dy, x+dx
            # 체스판 크기를 넘지 않고 방문 하지 않았을 경우 
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == -1:
                q.append((ny, nx)) # 좌표 이동
                graph[ny][nx] = graph[y][x]+1 # 방문 표시(방문한 횟수)
    



n = int(input())
# 출발지, 목적지 좌표 
r1, c1, r2, c2 = map(int, input().split())
# 방문 여부 확인
graph = [[-1] * n for _ in range(n)] 
# 데스나이트 이동 방향 좌표
deathNight = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

bfs(r1, c1)

print(graph[r2][c2]) # 데스나이트가 목적 좌표에 도달 했을때 방문표시 횟수(방문 횟수) 출력, 방문한 적이 없다는 것은 이동할 수 없다는 것이기 때문에 -1 그대로 출력 
