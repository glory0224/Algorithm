# 백준 1107번 리모컨 문제 
# import sys

# input = sys.stdin.readline

# # 현재 채널 위치 
# now_lation = 100

# # 사용 가능한 버튼 
# use_button = []

# # 이동할 채널 입력 
# N = map(int, input().split())

# # 고장난 번호와 비교할 리스트 생성 
# Check_N = list(map(str, N))

# # 고장난 번호 개수 
# T = int(input())

# # 고장난 번호 목록 
# ban = list(map(int, input().split()))

# # 고장난 번호를 제외하고 사용 가능한 번호 저장 
# for i in range(10):
   
#     if i == ban[0] or i == ban[1] or i == ban[2]:
#         pass
#     else:
#         if 
#         use_button.append(i)


# print(ban)
# print(use_button)

# 위의 코드는 내 삽질의 흔적.. 변수를 너무 많이 선언해서 코드가 산으로 갔다. 최대한 간결하게 코드를 참조하여 다시 아래에 정리한다. 

import sys
input = sys.stdin.readline

# 이동하고자 하는 목표 번호 
target = int(input())
# 금지할 번호 개수 
n = int(input())
# 금지할 번호 
break_num = list(map(int, input().split()))

# 현재 채널(100)에서 +와 -만 사용하여 이동하는 경우 
min_count = abs(100 - target)

# 문제에서 주어진 범위 값은 500000이지만 채널 자체는 무한대까지 입력 가능하고 만약 입력 받는 값에 500000 오게 되고 
# 1과 5만 사용 가능한 번호라고 한다면 155,555에서 500000 가는 것(+ 약 300000번)
# 511,111에서 500000 가는 것(+ 약 10000번)이 최소값이 되기 때문에 범위를 일부러 1000000까지 준다. 
for nums in range(1000001):
    # len 함수를 사용하기 위해서 str로 바꿔준다. 
    nums = str(nums)
                   # 0 ~ 999999
    for j in range(len(nums)):
        # print(nums[j])
        # 각 숫자의 버튼이 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in break_num:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            
            min_count = min(min_count, abs(int(nums) - target) + len(nums))#(min_count,현재채널에서 목표채널로 가기위한 버튼 클릭 횟수)
            print(min_count)
print(min_count)



