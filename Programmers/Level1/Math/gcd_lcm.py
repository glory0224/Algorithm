# 최대공약수와 최소공배수

# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수

import math

def find_gcd(n, m):
    return math.gcd(n, m)

def find_lcm(n, m):
    gcd = find_gcd(n, m)
    lcm = (n * m) // gcd # n과 m을 곱한 값을 최소공배수로 나눈다.
    return lcm


def solution(n, m):
    answer = []

    gcd = find_gcd(n, m)
    lcm = find_lcm(n, m)

    answer.append(gcd)
    answer.append(lcm)

    return answer

print(solution(3, 12))
print(solution(2, 5))