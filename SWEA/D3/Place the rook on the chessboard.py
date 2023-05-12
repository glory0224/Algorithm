# 체스판 위의 룩 배치 - 백트래킹으로 해결이 가능한가?

# 8 x 8 크기의 체스판 위의 몇 개의 칸에 룩(rook)이 놓여 있다. 각 칸에는 최대 1개의 룩을 놓을 수 있으므로, 체스판 위에는 0개 이상 64개 이하의 룩이 놓여 있는 것이다.
# 이때, 현재 체스판의 배치가 다음 조건을 모두 만족하는지를 판별하는 프로그램을 작성하라.
#     - 정확히 8개의 룩이 있어야 한다.
#     - 모든 룩은 서로 공격할 수 없어야 한다. 즉, 서로 다른 두 룩은 같은 열에 있거나 같은 행에 있으면 안 된다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 여덟 개의 줄로 이루어지며, 각 줄에는 길이가 8인 ‘O’ 또는 ‘.’로 구성된 문자열이 주어진다. i번째 줄의 j번째 글자는, 체스판의 i행 j열에 룩이 하나 놓여 있다면 ‘O’, 아무것도 놓여 있지 않다면 ‘.’이다.

# [출력]
# 각 테스트 케이스마다, 주어진 체스판의 배치가 주어진 모든 조건을 만족한다면 ‘yes’를, 하나라도 만족하지 않는다면 ‘no’를 출력한다.

# 입력
# 3
# ......O.
# .......O
# ...O....
# O.......
# ....O...
# ..O.....
# .O......
# .....O..
# OOOOOOOO
# OOOOOOOO
# OOOOOOOO
# OOOOOOOO
# OOOOOOOO
# OOOOOOOO
# OOOOOOOO
# OOOOOOOO
# .O.O.O.O
# O.O.O.O.
# ........
# ........
# ........
# ........
# ........
# ........

# 출력
# #1 yes
# #2 no
# #3 no

def check_rook(chess):

    # 좌표 체크용 리스트
    check = []

    # chess 를 2중 반복문으로 돌면서 'O'에 해당하는 좌표 저장
    for i in range(8):
        for j in range(8):
            if chess[i][j] == 'O':
                check.append((i, j))
    
    # 해당 좌표를 저장할 리스트 각각 초기화
    col = []
    row = []

    # check 에서 해당 행, 열에 해당하는 좌표값 각 리스트에 넣는다. 
    for i in range(len(check)):
        col.append(check[i][0])
        row.append(check[i][1])
    
    # 만약 row나 col의 길이가 8과 같고 중복이 없다면 true 아니면 false 반환
    if len(row) == 8 and len(col) == 8 and len(set(row)) == 8 and len(set(col)) == 8:
        YN = 'yes'
    else:
        YN = 'no'
    
    return YN

T = int(input())

YN = []

for _ in range(T):
    chess = [list(map(str, input())) for _ in range(8)]
    YN.append(check_rook(chess))

for i in range(T):
    print(f"#{i+1} {YN[i]}")

# ========================= 다른 풀이 방식 ================

T = int(input())

def count():
    # 8 * 8 행, 열 0 으로 초기화 
    row = [0, 0, 0, 0, 0, 0, 0, 0]
    col = [0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0 # 룩 개수 확인

    # 체스판 돌면서 확인
    for i in range(8):
        for j in range(8):
            if rook[i][j] == 'O': # 체스판에 룩이 놓여진 경우
                row[i] += 1 # 해당 행 증가
                col[j] += 1 # 해당 열 증가
                cnt += 1 # 룩 개수 추가
                if row[i] >= 2 or col[j] >= 2: # 중복 확인 
                    return False # 중복이면 False
            
    if cnt == 8: # 룩이 다 놓여진 경우
        return True
    else:
        return False
    

for tc in range(1, T+1):

    rook = [list(input()) for _ in range(8)]

    if count():
        print(f"#{tc} yes")
    else:
        print(f"#{tc} no")

