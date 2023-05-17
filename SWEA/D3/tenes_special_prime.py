# 테네스의 특별한 소수

# 테네스는 소수를 좋아한다. 소수란 1과 자기 자신만으로 나뉘어 떨어지는 숫자로 작은 것부터 나열하면 2, 3, 5, 7, 11, 13, 17, 19, 23, …같은 수들이 있다.

# 또한 테네스는 D를 포함하는 숫자도 좋아한다. 그렇기에 소수가 D를 포함하면 더욱 더 좋아하여 특별한 소수라고 부르기로 했다.

# 예를 들어 D = 3이면 3, 13, 23, … 같은 소수들이 3을 포함하였으므로 테네스는 이런 숫자들을 특별한 소수라고 부를 것이다.

# D가 주어질 때, A이상 B이하의 수 중에서 특별한 소수인 것들의 개수를 구하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 세 정수 D, A, B(1 ≤ D ≤ 9, 1 ≤ A ≤ B ≤ 106)가 공백으로 구분되어 주어진다.

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별한 소수의 개수를 출력한다.

# 입력

# 2
# 3 10 30
# 7 1 1000000

# 출력
# #1 2
# #2 43506

# 1. 입력받은 A와 B 소수를 먼저 판단 - 그 소수 중에서 D가 포함된 횟수 출력 문제

# 에라토스테네스의 채
def eratos_prime(n):

    is_prime = [True] * (n + 1)

    # 0과 1은 소수가 아니므로 제외
    is_prime[0] = is_prime[0] = False

    
    p = 2

    while p * p <= n: # 제곱이 n을 넘어가지 않는 범위 내
        if is_prime[p]: # 소수인 경우
            for i in range(p*p, n+1, p):
                is_prime[i] = False
            
        p += 1
    
    primes = [i for i in range(n+1) if is_prime[i]]

    return primes

# 일정 범위 소수에서 D 찾기
def find_prime_digit(D, A, B):
    # B가 최대 범위이므로 B까지의 소수를 판별
    primes = eratos_prime(B)

    # D가 포함되는 소수 개수
    cnt = 0

    for prime in primes:
        if prime < A: # A의 범위보다 작은 경우는 pass
            continue

        if str(D) in str(prime):
            cnt += 1

    return cnt



T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())

    # D가 포함된 소수 개수 반환
    cnt = find_prime_digit(D, A, B)

    print(f"#{tc} {cnt}")

    