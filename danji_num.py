# 백준 2667번 단지 번호 붙이기 
# BFS 방식 

import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

# 입력을 받아줄 그래프 선언
graph = []
# 결과를 담을 리스트 선언
result = []

# 2차원 배열로 입력 받아준다.
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
                 
# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque() # 큐 선언
    queue.append([a, b]) # a, b를 큐에서 그대로 빼내기 위해 append로 추가를 해준다.
    graph[a][b] = 0 # 첫번째 집 a,b를 방문 처리를 한다.
    count = 1 # 첫번째 집 a,b를 방문했기 때문에 count는 1부터 시작한다.

    while queue:
        x, y = queue.popleft()  # 큐에 들어간 좌표 x,y를 파이썬 문법을 활용하여 그대로 빼준다.
        graph[x][y] = 0
        for i in range(4): # 각 좌표마다 위 아래 왼쪽 오른쪽으로 이동시킨다.
            nx = x + dx[i]
            ny = y + dy[i]

            # 만약 좌표 이동을 한 후에 그래프의 범위를 벗어나는 경우 체크
            if nx < 0  or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
                
            if graph[nx][ny] == 1:
               graph[nx][ny] = 0
               queue.append([nx, ny])
               count += 1
               
    return count

# 그래프의 원소가 1일 때 bfs로 집을 방문한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

result.sort()  # 오름차순으로 정렬

print(len(result))  # 총 단지수 출력
for k in result:  # 각 단지마다 집의 수 출력
    print(k)
