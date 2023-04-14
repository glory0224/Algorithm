# 합성수 찾기 

def solution(n):

    # 소수를 구함(아리스토테네스의 채 이용)
    # 소수의 배수를 카운트함

    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2*i,n+1, i):
            if prime[j]:
                prime[j] = False
            
    
    # 소수의 배수가 False인 수(합성수) 개수 카운트
    count = 0

    for i in range(2, n+1):
        if not prime[i]:
            count += 1
    
    return count

print(solution(10))
