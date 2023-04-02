# 백준 1377번 버블 소트 문제 


# import sys

# input = sys.stdin.readline

# T = int(input())
# cnt = 0

# def bubble_sort(list):
#     global cnt
#     unsorted_until_index = len(list) - 1
#     sorted = False

#     while not sorted:
#         sorted = True
#         for i in range(unsorted_until_index):
#             if list[i] > list[i+1]:
#                 sorted = False
#                 list[i], list[i+1] = list[i+1], list[i]

#         cnt = cnt + 1        
#         unsorted_until_index = unsorted_until_index - 1


# bubble_list = []

# for i in range(T):
#     bubble_list.append(int(input()))

# bubble_sort(bubble_list)
# print(cnt)

# 위의 코드는 시간초과 

    
# 참고 코드

import sys

input = sys.stdin.readline

T = int(input())

nums = []


for i in range(T):
    num = int(input())
    nums.append((num, i)) # 튜플 형태로 append를 받고 인덱싱의 과정을 축소해 시간을 줄여본다.

sorted_nums = sorted(nums)
# print("sorted_nums : " + str(sorted_nums))

answer = 0
for i in range(T):
    #print(sorted_nums[i][1])
    #print("sorted_nums[ " + str(i) + " ][1] - " + str(i) + "+ 1 " )
    answer = max(sorted_nums[i][1] - i + 1, answer)

print(answer)

    
