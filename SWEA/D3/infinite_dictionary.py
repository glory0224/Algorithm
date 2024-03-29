# 무한 사전

# 영어 알파벳으로 만들 수 있는 모든 단어(그것이 뜻이 없어도)가 수록된 무한 사전이 있다.
# 두 단어 P, Q가 주어질 때, 사전 상에서 P와 Q사이에 다른 단어가 있는지 없는지 판별하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자로 이루어진 단어 P가 주어진다.

# 두 번째 줄에는 알파벳 소문자로 이루어진 단어 Q가 주어진다.
# P와 Q의 길이는 1이상 10이하이며, P는 Q보다 사전 상에서 먼저 오는 단어다.
# (단, 사전에는 10자보다 더 긴 단어가 존재 할 수 있다.)

# [출력]
# 각 테스트 케이스마다 용사가 사전 상에서 P와 Q사이에 다른 단어가 있다면 “Y”를, 아니면 “N”를 출력한다.

# 입력
# 2
# cat
# dog
# man
# mana

# 출력
# #1 Y
# #2 N

T = int(input())

answer = []
for tc in range(1, T+1):

    P = input().strip()
    Q = input().strip()

    # 소문자 첫 문자인 a가 P 다음에 왔는데 그 문자가 Q와 같으면 다른 단어가 올 수 없다.
    # 아니라면 올 수 있다.
    if P + 'a' != Q:
        print(f"#{tc} Y")
    else:
        print(f"#{tc} N")