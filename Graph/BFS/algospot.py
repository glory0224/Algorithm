# 백준 1261번 문제 알고스팟 

# https://velog.io/@aonee/%EB%B0%B1%EC%A4%80-boj-1261-%EC%95%8C%EA%B3%A0%EC%8A%A4%ED%8C%9F-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 데크의 특성을 이용해서 bfs로 풀 수 있는 문제 

from collections import deque

M, N = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
# 가중치
dist = [[-1] * M for _ in range(N)]

# 탐색 좌표 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0))
dist[0][0] = 0 # 시작점 가중치 0으로 초기화

while q:
    x, y = q.popleft()
    print(dist[x][y])
    for k in range(4): # 4 방향에 대한 탐색 
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if dist[nx][ny] == -1: # 탐색하면서 가중치가 -1일때만
                if miro[nx][ny] == 0: # 빈 방인 경우 : 0->0 가중치:0
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny)) # 데크를 이용해서 왼쪽 맨앞에 값을 저장
                else: # 벽이 있는 경우 :  0->1 가중치:1 ,  1->1 가중치:1
                    dist[nx][ny] = dist[x][y] + 1 # 벽을 부수는 횟수를 가중치로 설정했기 때문에 + 1씩
                    q.append((nx, ny)) # 데크를 이용해 오른쪽 끝에 저장


print(dist[N-1][M-1]) # 시작 값이 0부터 시작하면서 순차적으로 bfs를 하기 때문에 목적지인 인덱싱의 마지막은 -1 처리 

