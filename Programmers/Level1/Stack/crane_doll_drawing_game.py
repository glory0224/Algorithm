# 크레인 인형뽑기 게임
# 전형적인 스택 문제

def solution(board, moves):
    answer = 0
    
    # 크레인이 집어서 옮길 바구니 
    basket = []

    # 이동할 열을 확인
    for move in moves:
        # 행의 길이만큼 for문을 돌면서 열의 위치를 move 값으로 변경한다.
        for i in range(len(board)):
            # 인형 변수에 담기
            doll = board[i][move-1] # move는 1부터 시작하기 때문에 -1 한다.

            # 인형이 존재하면서
            if doll != 0:
                if basket and basket[-1] == doll: # 스택이 존재하고 스택의 맨 위의 값이 doll과 동일하면
                    basket.pop() # 제거
                    answer += 2 # 제거된 인형 개수 추가
                else:
                    basket.append(doll)
                
                board[i][move-1] = 0 # 해당 인형에 대한 처리 후 0 변경
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # result = 4