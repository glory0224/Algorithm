# 피보나치 수 


# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# 예를들어

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.


# case 1) 테스트 케이스는 통과하나 채점을 하면 런타임 에러가 발생

# def fibo(n):

#     # 0과 1인 경우 n을 그대로 반환
#     if n in [0, 1]:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

# def solution(n):
#     return fibo(n) % 1234567



# case 1이 런타임이 발생하는 이유

# fibo(5) 경우를 예를 들면 중복된 피보나치 수까지 재귀함수가 돌아가서 에러가 발생한다. 

    #          5   
    #     3         4
    #   1   2    2     3
    # 0   0  1  0  1  1  2
    #                    0 1

# case 2) dp 방식을 이용해서 이전에 저장된 값은 재귀 없이 바로 반환하도록 한다. 이때 파이썬의 재귀는 depth에 제한이 있어서 풀어준다.
# import sys

# def fibo(n, dp):

#     if n in [0, 1]:
#         return n
#     elif dp[n]: # dp에 해당 수가 채워져 있으면 그 수를 반환
#         return dp[n]
#     else:
#         # 계산한 값을 dp[n]에 추가
#         dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
#         return dp[n]

# def solution(n):
#     # dp 선언
#     dp = [0 for _ in range(n+1)]
#     dp[1] = 1 # 1은 1로 채운다.
#     sys.setrecursionlimit(999999) # depth 증가
#     return fibo(n, dp) % 1234567


# case 3) 브루트 포스 방식

def solution(n):
    save = [0 for __ in range(n+1)]
    save[1] = 1
    for idx in range(2, n+1):
        save[idx] = save[idx-1] + save[idx-2]
    
    return save[n] % 1234567

# case 4) case 3 개선 (리스트를 사용하지 않기 때문에 메모리를 더 절약 가능)

# def solution(n):
#     if n in [0, 1]:
#         return n
#     else:
#         pp, p = 0, 1 # 2부터 시작하기 때문에 전전과 전은 0과 1
#         for i in range(2, n+1):
#             pp, p = p, p+pp #전전의 수가 전의 수가 되고 전의 수가 전전과 전의 수 더한 값
        
#         return p % 1234567



print(solution(3)) # 2
print(solution(5)) # 5