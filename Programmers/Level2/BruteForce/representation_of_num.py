# 숫자의 표현

# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

def solution(n):
    answer = 0 # 경우의 수
    start = 1 # 시작 값

    while start <= n:
        total = 0 # 연속한 자연수의 합
        i = start #  연속적으로 더할 자연수 시작 값 계속 갱신

        while total < n: # n보다 작을 때까지만 자연수 더함
            total += i
            i += 1
        
        if total == n: # 합이 n이 나와야 +1
            answer += 1
        
        # 아니라면 시작하는 자연수 1 증가
        start += 1
    
    return answer

print(solution(15)) # 4