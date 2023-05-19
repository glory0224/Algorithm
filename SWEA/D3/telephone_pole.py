# 10580번 전봇대 문제

# 현우는 길을 가다가 전선들이 복잡하게 꼬여 있는 전봇대 두 개를 보았다. 두 전봇대는 높이가 매우 높으며, N개의 팽팽한 전선으로 연결되어 있었다. 두 전선이 끝점이 같은 경우는 없으나, 교차하는 경우는 있다. 이를 그림으로 하면 아래와 같다. (전선 3개가 있으며, 교차점 2개가 검은색으로 칠해졌다.)

# 세 개 이상의 전선이 하나의 점에서 만나지 않는다고 가정하자. 이 전봇대에는 총 몇 개의 교차점이 있을까?

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.

# 첫 번째 줄에 주어지는 전선의 개수 N이 주어진다 (1 ≤ N ≤1000).

# 이후 N개의 줄에 두 양의 정수 Ai, Bi 가 주어진다. (1 ≤ Ai, Bi ≤ 10000)이는 i번째 전선이, 첫번째 전봇대의 Ai cm 고도에 걸려 있고, 두 번째 전봇대의 Bi cm 고도에 걸려 있음을 뜻한다.

# 모든 Ai는 서로 다르고, 모든 Bi 도 서로 다르다. (두 전선의 끝점이 같은 경우가 없기 때문이다.) 세 전선이 한 점에서 만나지 않게 입력이 주어진다.

# [출력]
# 각 테스트 케이스마다 한 줄씩 교차점의 개수를 출력하라.

# 입력
# 2
# 3
# 1 10
# 5 5
# 7 7
# 2
# 1 1
# 2 2

# 출력
# #1 2
# #2 0

def count_intersection(lines):
    
    intersection_count = 0 # 교차점 개수

    # 2차원 배열 돌면서 각각 좌표 뽑기
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            x1, y1 = lines[i]
            x2, y2 = lines[j]

            # 선의 교차점이 생기는 경우
            # x1 < x2 and y1 > y2 (왼쪽 아래 -> 오른쪽 위 대각선)
            # x1 > x2 and y1 < y2 (왼쪽 위 -> 오른쪽 아래 대각선)

            if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
                intersection_count += 1

    return intersection_count            




T = int(input())

for tc in range(1, T+1):

    N = int(input())

    lines = []

    # 좌표 담기
    for i in range(N):
        a, b = map(int, input().split())

        lines.append((a, b))
    
    # 교차점 찾는 함수 작성

    result = count_intersection(lines)

    print(f"#{tc} {result}")



