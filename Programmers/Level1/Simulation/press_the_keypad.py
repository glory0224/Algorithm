# 키패드 누르기

# 시뮬레이션 문제 같은데..

# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.


# bfs 방식?

# def solution(numbers, hand):
#     answer = ''

#     left_location = 0
#     right_location = 0

#     # 상하좌우
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]


#     for i in range(len(numbers)):
#         # 왼쪽 경우
#         if numbers[i] in [1, 4, 7]:
#             answer += 'L'
#             left_location = numbers[i]
#         # 오른쪽 경우 
#         elif numbers[i] in [3, 6, 9]:
#             answer += 'R'
#             right_location = numbers[i]
#         # 가운데 경우
#         else:
#             # 위치가 왼쪽이 더 큰 경우
#             if abs(left_location - numbers[i]) > abs(right_location - numbers[i]):
#                 answer += 'R'
#             # 오른쪽이 더 큰 경우
#             elif abs(left_location - numbers[i]) < abs(right_location - numbers[i]):
#                 answer += 'L'
#             # 동일한 경우 왼손잡이, 오른손잡이로 구분
#             else:
#                 if hand == 'right':
#                     answer += 'R'
#                 else:
#                     answer += 'L'

#     return answer

# 문제 풀이 포인트는 좌표 딕셔너리를 사용하는 것, L 또는 R을 더해주는 순간마다 왼쪽 좌표와 오른쪽 좌표를 초기화 해주는 것

def solution(numbers, hand):
    answer = ''
    # 숫자들의 위치
    num2pos = {1:(0,0), 2:(0,1), 3:(0,2), 
               4:(1,0), 5:(1, 1), 6:(1, 2), 
               7:(2, 0), 8:(2, 1), 9:(2, 2), 
                        0:(3,1)}
    
    # 왼쪽 숫자 좌표 (* 의 좌표에서 시작)
    LH = (3,0)
    # 오른쪽 숫자 좌표 (# 의 좌표에서 시작)
    RH = (3,2)

    for number in numbers:
        # 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
        NP = num2pos[number]

        if number in [1, 4, 7]:
            answer += "L"
            # 왼쪽 방향 초기화
            LH = NP
        elif number in [3, 6, 9]:
            answer += "R"
            # 오른쪽 방향 초기화
            RH = NP
        else:
            # 왼쪽 거리, 오른쪽 거리 구하기
            
            # 현재 오른손과 왼손의 좌표에서 입력할 번호의 좌표의 절대값을 각각 빼주면 왼손 좌표와 오른손 좌표의 위치를 구할 수 있다.
            LHD, RHD = abs(LH[0] - NP[0]) + abs(LH[1] - NP[1]), abs(RH[0] - NP[0]) + abs(RH[1] - NP[1])

            if LHD < RHD:
                answer += 'L'
                # 왼쪽 방향 초기화
                LH = NP
            elif RHD < LHD:
                answer += 'R'
                # 오른쪽 방향 초기화
                RH = NP
            else: # 거리가 같은 경우
                if hand == 'left':
                    answer += 'L'
                    # 왼쪽 방향 초기화
                    LH = NP
                else:
                    answer += 'R'
                     # 오른쪽 방향 초기화
                    RH = NP


    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
         
