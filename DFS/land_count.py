# 백준 4963번 섬의 개수 

import sys

input = sys.stdin.readline
# 파이썬 재귀 함수 구현시 필수로 적기 
sys.setrecursionlimit(10000)

# 핵심은 대각선으로 이동하여 확인하는 dfs 구현 
def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1,-1, -1, 1, -1]
    
    # 방문했던 곳은 되돌아오면서 check 중복을 방지하기 위해 0처리, 만약 방문을 했던 곳이면 아래 dfs가 실행되지 않는다. 
    landmap[x][y] = 0
    # 대각선 방향까지 포함하여 이동하는 for문
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 지도 범위 내에 존재하고 그 값이 1과 같으면 dfs로 재귀적 실행 
        if 0 <= nx < h and 0 <= ny < w and landmap[nx][ny] == 1:
            dfs(nx, ny)

        
while True: 
    # 지도 크기 map함수로 받아줌
    w, h = map(int, (input().split()))
    # 입력의 마지막 줄에는 0이 두 개 주어진다. -> while함수 종료조건
    if w == 0 and h == 0:
        break
    # 입력 받을 지도 저장 변수 
    landmap = []
#     # 결과를 담을 리스트를 선언
#     result = []
    # 세어줄 개수
    count = 0
    # landmap에 입력값 높이만큼 반복문으로 추가 
    for _ in range(h):    
        landmap.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            # 섬에 해당하는 경우에 dfs 실행 
            if landmap[i][j] == 1:
                    dfs(i, j)
                    count += 1
    print(count)


