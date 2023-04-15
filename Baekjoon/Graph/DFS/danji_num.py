# 백준 2667번 단지 번호 붙이기 
# DFS 방식 

import sys

input = sys.stdin.readline
# 입력받을 2차원 배열 담아줄 리스트 선언
board = []
# 결과를 담을 리스트를 선언
result = [] 
count = 0
T = int(input())

for i in range(T):
    # [['0110100'], ['0110101'], ['1110101'], ['0000111'], ['0100000'], ['0111110'], ['0111000']]
    # board.append(list(input().split()))
    
    # [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
    board.append(list(map(int, input().rstrip()))) 

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표를 설정한다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global count
    
    # 범위를 초과하면 종료
    if x < 0 or x >= T or y < 0 or y >= T:
        return
    
    if board[x][y] == 1:
        count += 1
        board[x][y] = 0 # 되돌아오면서 갔던 곳은 못가도록 0으로 초기화 하여 중복 방지
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
    
        

# 그래프의 원소가 1일때만 dfs로 집을 방문한다. 여기서 하나씩 돌면서 1인지 0인지 여부를 확인해야 하기 때문에 위에서 map 함수로 쪼개준다.
for i in range(T):
    for j in range(T):
        if board[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0
            
result.sort() # 오름차순 정렬

print(len(result)) # 총 단지 수 출력
for k in result: # 각 단지마다 집의 수 출력 
    print(k)  
    
    

    
