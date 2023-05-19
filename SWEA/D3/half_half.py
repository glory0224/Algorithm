#반반 

# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
#     ∙ 첫 번째 줄에 문자열 S가 주어진다.

# [출력]
# 각 테스트 케이스마다
#     ∙ 조건이 만족되면 “Yes”, 아니면 “No” 를 출력하라.

# 입력
# 5
# ABAB
# CCDD
# EFFE
# EEEE
# NONE

# 출력
# #1 Yes
# #2 Yes
# #3 Yes
# #4 No
# #5 No

T = int(input())

for tc in range(1, T+1):

    char_list = list(map(str, input()))

    char_list.sort()

    same_num = 0
    diff_num = 0

    for i in range(1, len(char_list)):
        if char_list[i-1] == char_list[i]:
            same_num += 1
        elif char_list[i-1] != char_list[i]:
            diff_num += 1
    
    if same_num == 2 and diff_num == 1:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")


