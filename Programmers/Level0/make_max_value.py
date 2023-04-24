# 최댓값 만들기 (2)

# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 제한사항

# -10,000 ≤ numbers의 원소 ≤ 10,000
# 2 ≤ numbers 의 길이 ≤ 100

# 입출력 예

# numbers	                    result
# [1, 2, -3, 4, -5]	            15
# [0, -31, 24, 10, 1, 9]	    240
# [10, 20, 30, 5, 5, 20, 5]	    600

import itertools
import sys

def solution(numbers):
    # 0으로 초기화 하는 것보다 좋은 방식
    answer = -sys.maxsize 

    for a, b in itertools.combinations(numbers, 2):
        answer = max(answer, a * b)

    return answer

print(solution([0,0,0,-1]))
