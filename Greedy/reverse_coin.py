# 백준 1285번 동전 뒤집기 
# https://my-coding-notes.tistory.com/532
# pypy 제출

"""
    아이디어
    1. 행과 열 둘 중 기준을 하나 잡는다.
    2. 행을 뒤집는 모든 경우의 수를 구한 뒤, 열을 차례대로 순회하며 뒤집었을 때 이득인 경우만 뒤집는다.
    3. 행을 뒤집는 연산을 최소화하기 위해 비트 마스크를 이용한다.
    
    각각의 행을 뒤집는 경우
    ex) n = 3
    
    000, 001, 010, 011, 100, 101, 110, 111
    
    총 8가지 = 2^n 가지로 존재 
"""

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

# 실제로 행을 뒤집지는 않고 행을 뒤집은 경우를 미리 만들어주고 복사만 한다. 
rev_board = [k[:] for k in board]

ans = n**2

 
for i in range(n):
    for j in range(n):
        if rev_board[i][j] == 'T':
            rev_board[i][j] = 'H'
        else:
            rev_board[i][j] = 'T'

# print("1<<n : " + str(1<<n))

# 1에 해당하는 이진수 0001를 n만큼 왼쪽 시프트 -> 1000 -> 10진수 8 
for b in range(1<<n):
    tmp_board = []
    for i in range(n):
        # print(" b : " + str(b))
        # print(" 1 << i : " + str(1 << i))
        if b & (1 << i):
            tmp_board.append(rev_board[i][:])
        else:
            tmp_board.append(board[i][:])
            
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if tmp_board[j][i] == 'T':
                tmp += 1
        
        cnt += min(tmp, n-tmp)
    ans = min(ans, cnt)

print(ans)        
        
