# 백준 2206번 벽 부수고 이동하기
 
# https://hongcoding.tistory.com/18 

from collections import deque

n, m = map(int, input().split())
matrix = []

# # 3차원 행렬을 통해 벽의 파괴를 파악한다. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1 # 시작 방문 처리, 처음 bfs 함수 실행할 때 한번도 방문 하지 않은 if문을 타지 않기 위해 1 넣어둠

# print(visited)

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    matrix.append(list(map(int, input()))) # 2차원 행렬 만들기 

# print(matrix)

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        a, b, c = queue.popleft()
        # print("a : " + str(a) + " b : " + str(b) + " c : " + str(c))
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            # print("nx : " + str(nx))
            ny = b + dy[i]
            # print("ny : " + str(ny))
            # 탐색 가능 범위를 벗어날 경우 
            # print("--------------------------------")
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽 파괴 기회를 사용하지 않은 경우
            if matrix[nx][ny] == 1 and c == 0:
                # print("벽이고 벽 파괴 기회 사용 x")
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1)) # 벽 파괴 경우
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이라면
            elif matrix[nx][ny] == 0 and visited[nx][ny][c] == 0:
                # print("벽이 아니고 한번도 방문 x")
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))

        # print("shortest distance :  " + str(visited[a][b][c])) 
    return -1 # 도달 불가능한 경우 

print(bfs(0,0,0))

