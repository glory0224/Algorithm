# 소수 찾기 

# 에라토스테네스의 채를 이용한 소수 개수 찾기 

import math

def find_prime_count(n):
    # n까지 True로 된 리스트 
    is_prime = [True] * (n + 1)

    # 1과 0은 소수가 아님
    is_prime[0], is_prime[1] = False, False

    # 2부터 n의 제곱근까지 소수 판별
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i] == True: # 소수인 경우
            for j in range(i*2, n + 1, i): # 현재 소수의 배수는 소수가 아님
                print("j : ", j)
                is_prime[j] = False

    print("is_prime : ", is_prime)  
    count = sum(is_prime)

    return count


def solution(n):

    answer = find_prime_count(n)

    return answer

print(solution(10))
print(solution(5))

