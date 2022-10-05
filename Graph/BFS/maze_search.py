# 백준 2178번
# 참고하기 -  https://bmy1320.tistory.com/entry/%EB%B0%B1%EC%A4%80-Silver-1%EB%AC%B8%EC%A0%9C-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2178-%EB%AF%B8%EB%A1%9C-%ED%83%90%EC%83%89

# 


from collections import deque

N, M = map(int, input().split())

maze = []

for _ in range(N):
  maze.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # 벽이므로 진행 불가
      if maze[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return maze[N-1][M-1]

print(bfs(0, 0))

            
            
