# 백준16929번 Two Dots 문제 
# 게임판 상태에 따라 사이클이 존재하는지 아닌지 구하는 전형적인 dfs문제 

from sys import stdin
input = stdin.readline

N,M = map(int, input().split())
# 2차원 배열 입력받기
arr = [list(map(str, input())) for _ in range(N)] 
# 방문 여부 2차원 배열 생성
visited = [[False]*M for _ in range(N)]
# 확인할 방향 좌표
dy = [0,0,1,-1]
dx = [1,-1,0,0]

# 정답의 YES와 NO를 위한 flag 변수
flag=False

def scope(y, x):
    if y >=0 and y < N and x >= 0  and x < M:
        return True
    else:
        return False
    
def dfs(y, x, py, px, ball):
    # 만약 가다가 해당 조건이 만족해서 선이 연결된다면 True 반환 후 dfs 종료 
    if visited[y][x] == 1:
        return True
    
    visited[y][x] = True

    for i in range(4):
        ny = y  + dy[i]
        nx = x + dx[i]
        
        if nx!=px or ny!=py:
            # 범위를 넘지 않고 이동할 공의 색깔이 현재의 공의 색깔과 일치하는지 여부를 확인한다.
            if scope(ny, nx) and arr[ny][nx]==ball:
                if dfs(ny, nx, y, x, ball): return True
    # 4방향 모두 갈 수 없는 상황으로 false 반환 
    return False


# 2차원 배열을 돈다.
for i in range(N):
    for j in range(M):
        # 방문 했던 곳이면 continue
        if visited[i][j]:
            continue
        if dfs(i, j, 0, 0, arr[i][j]):
            flag=True
            break

print("Yes") if flag else print("No")

