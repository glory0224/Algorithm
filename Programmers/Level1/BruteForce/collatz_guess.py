# 콜라츠 추측 문제

# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

# 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

def solution(num):
    for i in range(500):
        if num == 1:
            return i
        elif num % 2:
            num = num * 3 + 1
        else:
            num //= 2
    
    return -1

print(solution(6)) # 8
print(solution(16)) # 4
print(solution(626331)) # -1
