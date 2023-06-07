# 약수의 개수와 덧셈

import math

# 약수의 개수를 세는 방법 1
# 하나씩 전부 비교

# def count_divisor(num):
#     count = 1 # 1은 모든 수의 약수
#     # 해당 num 까지 돌면서 약수 개수 세기
#     for i in range(2, num+1):
#         if num % i == 0:
#             count += 1
#     return count

# 약수의 개수를 세는 방법2
# 제곱근을 비교 (시간 단축)

def count_divisor(num):
    count = 0
    
    # 제곱근
    sqrt_num = int(math.sqrt(num))

    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            count += 2 # i와 n/i가 약수이므로 개수 2 증가
    
    if sqrt_num ** 2 == num: # 제곱근이 정수인 경우 중복 약수를 제거
        count -= 1

    return count

def solution(left, right):
    answer = 0

    # left부터 right의 범위까지
    for num in range(left, right+1):
        # 약수의 개수를 세는 함수 선언
        cnt = count_divisor(num)
        # 약수의 개수가 짝수인 경우 num 더함
        if cnt % 2 == 0:
            answer += num
        else: # 홀수인 경우 빼줌
            answer -= num
    
    return answer

print(solution(13, 17)) # result 43
print(solution(24, 27)) # result 52


