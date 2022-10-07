# 백준 7562번 나이트의 이동 
# https://bang-tori.tistory.com/27
# bfs 

import sys
from collections import deque

input  = sys.stdin.readline

T = int(input())

def bfs():
    # 나이트의 이동 좌표 표현
    # 현재 기준을 [0,0]으로 생각하고 아래 배열을 넣어보면 이해가 쉽다.
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((startX, startY))
    while q :
        x , y = q.popleft()
        # 목적지에 도달했을 때 bfs 종료 
        if x == endX and y == endY:
            # 시작값을 1부터 시작했기 때문에 마지막 return은 -1 
            return matrix[x][y] -1
        # 각 방향마다 확인하면서 bfs 실행
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 넘지 않고, 방문하지 않았던 곳일 경우만 bfs
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx, ny))
            
for _ in range(T):
    # 크기 받기 
    l = int(input().rstrip())
    # 출발 좌표 받기 
    startX, startY = map(int, input().rstrip().split())
    # 목적 좌표 받기 
    endX , endY = map(int,input().rstrip().split())
    # 해당 범위만큼의 2차원 배열 생성 
    matrix = [[0]*l for _ in range(l)]
    # 시작하는 곳은 최소값의 카운트에 포함되기 때문에 1로 시작해준다.
    matrix[startX][startY] = 1
    print(bfs())
