# 100만 이하의 모든 소수

# 소수 = 아리스토테네스의 채를 이용

# 1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

# 참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

# [입력]

# 이 문제의 입력은 없다.

# [출력]

# 1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

def find_prime(num):

    is_prime = [True] * (num + 1)

    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아니므로 false

    for i in range(2, int(num ** 0.5) + 1): # 2부터 num의 제곱근까지
        if is_prime[i]: # 소수인 경우
            for j in range(i*2, num+1, i): # 그 소수의 배수들은 모두 False
                is_prime[j] = False
        
    return [i for i in range(2, num + 1) if is_prime[i]] # 소수에 해당하는 수들만 리스트로 반환


print(" ".join(map(str, find_prime(10 ** 6))))

        