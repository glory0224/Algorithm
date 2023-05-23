# 공원 산책 문제

# 지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 공원에서 로봇 강아지가 산책을 하려합니다. 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 명령은 다음과 같은 형식으로 주어집니다.

# ["방향 거리", "방향 거리" … ]
# 예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다. 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

# 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
# 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
# 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
# 공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

# 공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ park의 길이 ≤ 50
# 3 ≤ park[i]의 길이 ≤ 50
# park[i]는 다음 문자들로 이루어져 있으며 시작지점은 하나만 주어집니다.
# S : 시작 지점
# O : 이동 가능한 통로
# X : 장애물
# park는 직사각형 모양입니다.
# 1 ≤ routes의 길이 ≤ 50
# routes의 각 원소는 로봇 강아지가 수행할 명령어를 나타냅니다.
# 로봇 강아지는 routes의 첫 번째 원소부터 순서대로 명령을 수행합니다.
# routes의 원소는 "op n"과 같은 구조로 이루어져 있으며, op는 이동할 방향, n은 이동할 칸의 수를 의미합니다.
# op는 다음 네 가지중 하나로 이루어져 있습니다.
# N : 북쪽으로 주어진 칸만큼 이동합니다.
# S : 남쪽으로 주어진 칸만큼 이동합니다.
# W : 서쪽으로 주어진 칸만큼 이동합니다.
# E : 동쪽으로 주어진 칸만큼 이동합니다.
# 1 ≤ n ≤ 9

# 입출력 예

#   park	                        routes	                result
# ["SOO","OOO","OOO"]	        ["E 2","S 2","W 1"]	        [2,1]
# ["SOO","OXX","OOO"]	        ["E 2","S 2","W 1"]	        [0,1]
# ["OSO","OOO","OXO","OOO"]	    ["E 2","S 3","W 1"]	        [0,0]


# 나는 routes를 딕셔너리 이용해서 풀이하려 했으나 리스트로도 풀이가 가능했다.

# https://velog.io/@m2nja201/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%B5%EC%9B%90%EC%82%B0%EC%B1%85-python-%EC%9E%85%EB%AC%B8

# def solution(park, routes):
#     answer = []
    
#     matrix = []
    
#     for p in park:
#         matrix.append(list(p))
    
#     # 리스트의 공백으로 구분된 문자를 딕셔너리로 저장
#     dic_routes = dict(map(lambda x: (x.split()[0], int(x.split()[1])), routes))
    
#     x, y = 0, 0

#     # 좌표의 초기 위치 S를 찾아야한다. 
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 'S':
#                 x, y = i, j
#                 break
    
#     dx , dy = x, y

#     # 해당 딕셔너리로 저장한 route를 돌면서 확인
#     for k, v in dic_routes.items():
        
#         if k == 'E':
#             # v 길이만큼 반복문 돌면서 해당 위치 정보 확인
#             for _ in range(v):
#                 dy += 1 # 행 증가
#                 # 조건문으로 갈 위치가 x이거나 matrix[0]의 범위(행)를 벗어나면 -1 
#                 if dy >= len(matrix[0]) or matrix[dx][dy] == 'X':
#                     dy = y
#                     break
        
#         elif k == 'S':

#             for _ in range(v):
#                 dx += 1 # 열 증가
#                 # 조건문으로 갈 위치가 x이거나 matrix(열)의 범위(행)를 벗어나면 -1 
#                 if dx >= len(matrix) or matrix[dx][dy] == 'X':
#                     dx = x
#                     break
        
#         elif k == 'W':

#             for _ in range(v):
#                 dy -= 1
#                 if dy < 0 or matrix[dx][dy] == 'X':
#                     dy = y
#                     break
        
#         elif k == 'N':

#             for _ in range(v):
#                 dx -= 1
#                 if dx < 0 or matrix[dx][dy] == 'X':
#                     dx = x
#                     break
        
#     answer.append(dx)
#     answer.append(dy)
    
#     return answer

def solution(park, routes):
    # idx
    x = 0
    y = 0

    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j # 행
                y = i # 열
                break
    

    
        # 찾은 시작점 x, y 를 기준으로 각 routes 명령을 실행한다.        
    for route in routes:
            
        # 위치 초기화
        xx = x
        yy = y

            # 문자열에서 문자 인덱스를 0,1,2 로 분기해서 각 조건 성립 시 이동
        for step in range(int(route[2])):
                # 방향과 일치하고 park 범위를 벗어나지 않는다면
            if route[0] == 'E' and xx != len(park[0]) - 1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(route[2]) - 1: # 해당 스텝만큼 움직였다면
                    x = xx # dx만큼 x를 갱신

            elif route[0] == 'W' and xx != 0 and park[yy][xx-1] != 'X':
                xx -= 1
                if step == int(route[2]) - 1:
                    x = xx

            elif route[0] == 'S' and yy != len(park) - 1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(route[2]) - 1:
                    y = yy

            elif route[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1

                if step == int(route[2]) - 1:
                    y = yy
  
    return [y, x]


print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))




    

    
