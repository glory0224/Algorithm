# 오목 판정 - 가능한 모든 경우의 수(브루트 포스)

# N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.

  

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.

# 다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.

  

# [출력]

# 각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.

# 입력
# 4
# 5
# ....o
# ...o.
# ..o..
# .o...
# o....
# 5
# ...o.
# ooooo
# ...o.
# ...o.
# .....
# 5
# .o.oo
# oo.oo
# .oo..
# .o...
# .o...
# 5
# .o.o.
# o.o.o
# .o.o.
# o.o.o
# .o.o.

# 출력
# #1 YES
# #2 YES
# #3 YES
# #4 NO

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    board = [input() for _ in range(n)] # 2차원 배열 생성
    

    result = 'No'
    # 2차원 배열을 돌면서 'o' 확인
    for i in range(n):
        for j in range(n):
            # 해당 범위를 벗어나지 않고 
            # 한 행이 전부 'o'
            if i <= n-5 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] == 'o':
                result = 'Yes'
            # 한 열이 전부 'o'
            if j <= n-5 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] == 'o':
                result = 'Yes'
            # 왼쪽 위, 오른쪽 아래 대각선 방향 전부 'o'
            if i <= n-5 and j <= n-5 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][i+4] == 'o':
                result = 'Yes'
            # 왼쪽 아래, 오른쪽 위 대각선 방향 전부 'o'
            if i <= n-5 and j <= n-5 and board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == board[i-4][i+4] == 'o':
                result = 'Yes'
    
    print(f"#{tc} {result}")
            


