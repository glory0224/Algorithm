# 백준 4963번 섬의 개수 

# bfs 풀이 

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    # 대각선 좌표까지 추가 
    dx = [-1, 1, -1, 1, 0, 0, -1, 1]
    dy = [-1, 1, 1, -1, 1, -1, 0, 0]
    landmap[x][y] = 0
    q = deque()
    q.append([x, y]) # 큐에 배열 형태로 담아준다.
    while q:
        a, b = q.popleft() # 파이썬 문법으로 빼준다.
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and landmap[nx][ny] == 1:
                landmap[nx][ny] = 0
                q.append([nx, ny])
    
while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    landmap = []
    count = 0
    for _ in range(h):
        landmap.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if landmap[i][j] == 1:
                bfs(i, j)
                count += 1
    
    print(count)    