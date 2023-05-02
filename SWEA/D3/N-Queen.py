# # N-Queen 문제

# 특정 조건을 만족하는 모든 경우의 수를 구함 - 백트래킹

# 8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다.

# 퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다. 이 문제의 한가지 정답은 아래 그림과 같다.
 

# 이 문제의 조금 더 일반화된 문제는 Franz Nauck이 1850년에 제기했다.

# N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 N(1 ≤ N ≤ 10)이 주어진다.


# [출력]

# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 입력받은 매개 변수의 위치에서 퀸을 놓을 수 있는지 확인 하는 메서드 필요

# 1. 퀀을 놓는 함수(백트래킹 재귀)

# 2. 퀸을 놓을 수 있는 경우를 반환하는 함수

# 3. 메인 코드

def is_valid(board, row, col):
    
    for i in range(row):

        if board[i] == col or abs(board[i] - col) == row - i: # 해당 행 기준으로 열과 대각선에 똑같은 값이 있는지 체크 
            return False
    
    return True



def place_queens(board, row, cnt):
    
    # 종료 조건 - 행이 board 길이와 같아지면 경우의 수 + 1 처리 후 종료
    if row == len(board):
        return cnt + 1

    for col in range(len(board)):
        # 현재 위치에 퀸을 놓을 수 있는지 확인
        if is_valid(board, row, col):
            board[row] = col # 퀸 배치
            cnt = place_queens(board, row + 1, cnt) # 다음 행 재귀함수 호출 

    return cnt


T = int(input())

for tc in range(1, T+1):
    
    queen_num = int(input())

    chess_board = [-1] * queen_num # 퀸 개수 만큼 보드판 생성
    # 경우의 수
    cnt = 0

    for col in range(queen_num):
        chess_board[0] = col # 첫번째 행에 퀸 정의
        cnt = place_queens(chess_board, 1, cnt) # 다음 행부터 시작
    
    print(f"#{tc} {cnt}")


    



