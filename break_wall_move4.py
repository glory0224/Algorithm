# 백준 16946번 벽 부수고 이동하기 4

# https://ku-hug.tistory.com/153


from collections import deque
input = __import__('sys').stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        a, b = q.popleft()
        zeros[a][b] = group
        for i in range(4):
            nx, ny = a + dy[i], b + dx[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or matrix[nx][ny] == 1:
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
            cnt += 1
    return cnt


n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().strip())))

# print(matrix)

visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {} # dic 저장
info[0] = 0


# 상하 좌우 

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            W = bfs((i, j))
            info[group] = W
            # print(" info [ " + str(group) + "]의 W값 : " + str(W))
            group += 1

for i in range(n):
    for j in range(m):
        addList = set()
        if matrix[i][j]:
            for idx in range(4):
                ni , nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                # print(info)
                # print("info [ " + str(add) + "] : " + str(info[add]))
                matrix[i][j] += info[add]
                # print("+= info[add] : " + str(matrix[i][j]))
                matrix[i][j] %= 10
                # print("%= 10: " + str(matrix[i][j]))

# print(matrix)

for m in matrix:
    print("".join(map(str, m)))