# 백준 14500번 테트로미노
# https://cijbest.tistory.com/87 코드 
# pypy3으로 풀기 
# dfs 개념 

import sys
input = sys.stdin.readline

# 상, 하, 좌, 우, 
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# INPUT
# N이 행(세로) , M이 열(가로)
N, M = map(int, input().split())
# 숫자 기록판
board = [list(map(int,input().split())) for _ in range(N)]
# 방문 횟수 확인 
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산(재귀 함수의 종료조건)
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]

        # 0과 입력한 범위를 벗어나지 않고 방문한 적이 없다면 
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            # cnt가 4가 되어 함수가 return 될 때, 방문했던 2차원 배열의 true 값을 이전 함수를 하나씩 종료하면서 False 값으로 돌려놓는다.
            visited[ni][nj] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산 , 따로 함수를 정의하고 구해주는 이유는 테트로미노는 상, 하, 좌, 우로 연달아 이동해야하는데 이 모양은 그렇게 할 수 없기 때문에 따로 경우의 수를 놓고 구해준다.
def exce(i, j):
    global maxValue
    # 마지막 배열의 인덱스 번호는 ㅗ,ㅜ,ㅏ,ㅓ 모양을 놓으려 할 때  가운데의 기준으로 놓을 수가 없다. 왜냐하면 4개의 방향 어디로 회전 시키든지 모양 한쪽이 비게 된다.(그림을 그려보면 쉽게 이해가 가능하다.) 
    # 따라서 이 모양에서는 0 ~ 3까지 그 안에서 0~2까지 돌면서 각각 회전 대칭의 모양을 놓을 수 있다. 
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301 (4가지 경우의 튀어나온 방향 구하기)
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        # 함수를 다 돌고나면 처음 값은 그대로 True 값을 유지하기 때문에 다음 값에서 이전 값을 비교 할 수 있도록 False로 바꿔준다.  
        visited[i][j] = False 

        exce(i, j)

print(maxValue)
    
