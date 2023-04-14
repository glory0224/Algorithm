# 팩토리얼 문제 

# 개선 코드

import sys
sys.setrecursionlimit(100000)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def solution(n):
    answer = 0
    
    if n == 1:
        answer = 1
    
    for i in range(2, n + 1):
        
        if factorial(i) > n:
            break
            
        answer = i
        
    return answer



# 나의 답

# import sys
# sys.setrecursionlimit(100000)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# def solution(n):
#     answer = 0
    
#     if n == 1:
#         answer = 1
    
#     for i in range(2, int(n ** 0.5) + 2):
#         if factorial(i) <= n:
#             answer = i
        
#     return answer