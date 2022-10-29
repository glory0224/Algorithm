# 백준 1744번 수 묶기 
# 그리디 알고리즘 


"""
    아이디어
    
    1. 수를 오름차순 정렬한 뒤 두 수를 곱하고 정답 값에 대입?
    
    - 반례 존재 
    
    n = 5
    -537
    81
    -435
    257
    157
    
    -> 오름차순 -537 -435 81 157 257
    -> (-537, -435), (81, 157), (257) 이렇게 묶이는데 (157 * 257)이 되어야 최대 값이 도출 되기 때문에 반례가 생긴다.
    
    2. 음수 , 양수, 1을 케이스별로 리스트를 나누어서 계산?
    
    - 음수는 오름차순 정렬, 양수는 내림차순 정렬, 1은 곱해도 의미가 없기 때문에 최대합을 위해 곱하기 대신 더하는 방식
    - (이때, 0은 음수에 속한다. 수 묶음이 (음수, 0)이 되어야 손해를 적게보니까)
    
    -> 코드 구성 
"""

# https://jokerldg.github.io/algorithm/2021/03/15/number-tie.html

import sys
input = sys.stdin.readline

N = int(input())
positive  = [] # 양수를 저장할 리스트
negative = [] # 음수를 저장할 리스트
max_sum = 0

for _ in range(N):
  n = int(input())
  
  if n > 1:
    positive.append(n)
  elif n == 1:
    max_sum += 1 # 1, 양수의 규칙에 의해 1을 더한다.
  else:
    negative.append(n)

positive.sort(reverse=True) # 양수의 큰 수부터 정렬한다.
negative.sort() # 음수의 작은 수부터 정렬한다.

# 양수 리스트 더해주기
if len(positive) % 2 == 0: # 양수가 짝수개 일경우 두개씩 곱해준다.
  for i in range(0, len(positive), 2):
    max_sum += positive[i] * positive[i+1]
else:
  for i in range(0, len(positive)-1, 2): 
    max_sum += positive[i] * positive[i+1]
  max_sum += positive[len(positive)-1] # 마지막 수는 더해준다.

# 음수 더해주기
if len(negative) % 2 == 0: # 음수가 짝수개 일경우 두개씩 곱해준다.
  for i in range(0, len(negative), 2):
    max_sum += negative[i] * negative[i+1]
else:
  for i in range(0, len(negative)-1, 2):
    max_sum += negative[i] * negative[i+1]
  max_sum += negative[len(negative)-1] # 마지막 수는 더해준다.

print(max_sum)



# https://data-flower.tistory.com/44

# n = int(input())

# # 음수, 양수, 1 리스트 만들기 

# minus_list = []
# plus_list = []
# one_list = []
# ans = 0 # 최대합 

# # 입력 값 받기 

# for i in range(n):
#     input_num = int(input())
#     if input_num > 1: # 양수
#         plus_list.append(input_num)
#     elif input_num <= 0: # 음수이거나 0
#         minus_list.append(input_num)
#     else:
#         one_list.append(input_num)
        
# plus_list.sort(reverse=True)
# minus_list.sort

# # 양수 계산 
# # 양수의 개수가 홀수라면 제일 작은 값을 정답에 더하기 
# if len(plus_list) % 2 == 1:
#     ans += plus_list[len(plus_list)-1] # 내림차순 정렬했기 때문에 제일 작은 값은 마지막 인덱스에 저장된 값
#     for j in range(0, len(plus_list)-1, 2):
#         ans += plus_list[j] * plus_list[j+1]
# # 양수의 개수가 짝수면 두 수를 곱하고 정답에 더하기 
# else:
#     for j in range(0, len(plus_list), 2):
#         ans += plus_list[j] * plus_list[j+1]

# # 음수 계산(0 포함)
# # 음수의 개수가 홀수라면 제일 작은 값을 정답에 더하기 
# if len(minus_list) % 2 == 1:
#     ans += minus_list[len(minus_list)-1]
#     for j in range(0, len(minus_list)-1, 2):
#         ans += (minus_list[j]) * (minus_list[j+1])
# # 음수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
# else:
#     for j in range(0, len(minus_list), 2):
#         ans += (minus_list[j]) * (minus_list[j+1])


# # 수 1에 대한 계산

# for j in range(len(one_list)):
#     ans += one_list[j]

# # 정답 출력
# print(ans)