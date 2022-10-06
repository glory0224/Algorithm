# 백준 7576번 토마토 문제 

#bfs

import sys
from collections import deque

input = sys.stdin.readline
# 가로 세로 입력 받기 
M, N = map(int, input().split())
# lack의 크기만큼 2차원 배열 생성
lack = [list(map(int,input().split())) for _ in range(N)]
# 좌표를 넣어줄 것이기 때문에 빈 배열을 담는다.
queue = deque([])
# 정답이 담기는 변수 
res = 0

# bfs로 이동할 방향을 나타내는 변수 설정
# 상, 하, 좌, 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]



# queue 배열에 처음에 받은 토마토의 위치를 append  
# N과 M의 사용을 헷갈리지 말아야한다.
# for문을 돌면서 시작을 토마토가 익어있는 상태인 1부터 시작할 수 있도록 한다.
for i in range(N):
    for j in range(M):
        if lack[i][j] == 1:
            # print("lack의 i번 index: " + str(i) +"lack의 j번 index: " + str(j) + "의 값 : " + str(lack[i][j]))
            queue.append([i, j])
    
def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
              
            # 이미 익은 토마토나 렉에 없는 토마토는 continue => 바깥에 이중 for문으로 확인
            # if lack[nx][ny] == 1 or lack[nx][ny] == -1:
            #     continue
            
            # 좌표의 크기를 넘지 않고 익지 않은 토마토일 경우 
            if  0 <= nx  < N and 0 <= ny < M and lack[nx][ny] == 0:
                
                lack[nx][ny] = lack[x][y] + 1
                queue.append([nx, ny])
                
bfs()

for i in lack:
    for j in i:
        # 다 돌았는데도 토마토가 익지 않았다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최대값이 정답        
    res = max(res, max(i))


# 위의 for문을 통해서 처음 시작을 1로 표현했으니 결과 값에서는 1을 빼준다.                
print(res-1)

