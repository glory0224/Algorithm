#소인수분해

def solution(n):
    answer = []
    prev = -1 # 첫 번째 소인수를 처리하는 경우와 구분되지 않기 때문에 -1로 초기화 

    # for i in range(2, int(n**0.5) + 1):
    #     while n % i == 0:
    #         if i != prev:
    #             answer.append(i)
    #             prev = i
    #         n = n // i
    #     if n == 1:
    #         break n이 1인 경우에는 중단할 필요가 없다.
    # 왜냐하면 이 경우에는 이미 모든 소인수를 구한 것이므로 더 이상 루프를 돌 필요가 없기 때문이다. 
            
    for i in range(2, int(n**0.5)+1): #아리스토테네스의 채 사용하여 소수를 빠르게 구함
        while n % i == 0:
            if i != prev:
                answer.append(i)
                prev = i
            n = n // i
        
    if n > 1 :
        answer.append(n)
    
    
    return answer