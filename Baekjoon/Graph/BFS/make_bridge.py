# 백준 2146번 다리 만들기
# bfs를 두번 이용하여 푸는 문제  
# https://kyun2da.github.io/2021/04/22/makeBridge/
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 지도를 입력 크기 만큼 그려주기
smap = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
count = 1
#아무리 큰 수라 할지라도 얼마든지 더 큰 수가 지정될 수 있으므로 변수에 임의의 큰 값으로 초기화 하는 것은 지양해야 하고 
# 그렇기 때문에 초기화를 위해 큰 수가 아닌 sys.maxsize로 초기화 한다. 
answer = sys.maxsize

# 위 아래 왼쪽 오른쪽으로 이동할 좌표 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 섬을 구분하기 위한 bfs - count를 이용해서 섬을 그룹화하여 구분한다.
def bfs1(i, j):
    global count 
    q = deque()
    q.append([i, j])
    # 방문 표시
    visited[i][j] = True
    smap[i][j] = count
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # bfs 탐색 
            if 0 <= nx < N and 0 <= ny < N and smap[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                smap[nx][ny] = count # 섬에 해당하는 곳을 번호로 표시 
                q.append([nx, ny])
                         
# 바다를 건너면서 가장 짧은 거리를 구한다.
def bfs2(z):
    global answer
    dist = [[-1] * N for _ in range(N)] # 거리가 저장될 배열
    q = deque()
    
    for i in range(N):
        for j in range(N):
            if smap[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0
                
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수가 없다면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 다른 땅을 만나면 기존 답과 비교해서 짧은 거리를 선택한다.
            if smap[nx][ny] > 0 and smap[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return
            
            # 바다를 만나면 dist를 1씩 늘린다.
            if smap[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
            


# 2차원 배열을 돌면서 섬을 그룹화 하여 구분 
for i in range(N):
    for j in range(N):
        if not visited[i][j] and smap[i][j] == 1:
            bfs1(i, j)
            count += 1 # 다음 bfs1을 수행할 때 그룹화 하기 위해 번호 + 1

# 해당 그룹까지         
for i in range(1, count):
    # print(count)
    bfs2(i)
    
print(answer)
