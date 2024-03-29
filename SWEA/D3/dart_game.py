# 다트 게임 - 구현 문제

# 보드에 그려진 다트 게임을 생각해보자. 보드에는 중심이 원점이고 반지름이 20,40,60,80,100,120,140,160,180,200 (단위는 mm)인 10개의 원이 그려져 있다.
# 각각의 화살은 꽂힌 지점을 감싸는 가장 가까운 원(경계선에 꽂힌 경우도 포함)의 반지름이 20 * (11 - p)인 경우 p점을 획득한다. (1 ≤ p ≤ 10)
# 만약 가장 큰 원 바깥에 꽂혔다면 얻는 점수는 없다. N 개의 화살을 던진 위치가 주어지면, 총 몇 점을 얻었는지 계산하자.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다. 
#     -  첫 번째 정수는 화살의 개수 N이다. (1 ≤ N ≤ 1000000)
#     -  이후 화살이 떨어진 위치 (x, y) 가 두 정수로 주어진다. (-200 ≤ x, y ≤ 200)

# [출력]

# 각 테스트 케이스마다 점수의 합을 출력하라.

# 입력
# 1
# 5
# 80 -14
# 117 12
# 98 -69
# -86 21
# -121 99

# 출력
# #1 25

# 유클리드 거리 공식을 활용한 반지름을 구하고 그 것을 활용하여 문제 풀이

import math

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    # 초기화할 총점
    total = 0

    # 정답 리스트 

    ans = []

    for n in range(N): # 다트 개수만큼 반복
        x, y = map(int, input().split())
        # 좌표를 유클리드 거리를 활용해서 20으로 나눠서 반지름 구함 (소수점 단위는 올림처리)
        # math.sqrt(x*x + y*y) 
        r = math.ceil(math.sqrt(x*x + y*y) / 20)

        # 반지름이 0 이하인 경우 기본 점수 10점 
        if r <= 0:
            total += 10
        elif r <= 11:
            total += 11 - r # 11 이하인 경우 11 - r
        # 정답에 추가
    
    ans.append(f"#{tc} {total}")

    
    # 리스트에서 출력
    for x in ans:
        print(x)








    
