# 백준 14502번 연구소 문제

from collections import deque
import copy

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph) # 원본 그래프의 값이 변경되지 않고 유지시키기 위한 깊은 복사
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        # 인접 간선 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0 # 감염되지 않은 연구소 칸을 세기 위한 변수 

    for i in range(N):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)
    # print("bfs answer : " + str(answer))


# 모든 경우의 수에 대한 벽을 세워야 하기 때문에 벽을 세우고 BFS를 수행한 후 벽을 지우고
# 그 다음칸에 대해 다시 벽을 세우고 BFS를 수행하고 벽을 지우는 방식을 반복해야 한다.
# 백트레킹 방식을 이용
def makeWall(cnt):
    # print("cnt : " + str(cnt))
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                # print("graph ["+str(i)+"] ["+str(j)+"] = " + str(graph[i][j]))
                makeWall(cnt + 1)
                graph[i][j] = 0
                # print("return graph ["+str(i)+"] ["+str(j)+"] = " + str(graph[i][j]))


N, M = map(int, input().split())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))

# print(graph)

answer = 0
makeWall(0) # 벽을 세우는 함수 
print(answer)
