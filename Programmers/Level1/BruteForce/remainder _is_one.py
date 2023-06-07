# 나머지가 1인 수
# n은 3 ~ 1000000 사이 수
# i는 1을 제외한 2부터 돌면서 제일 먼저 나온 수가 제일 작은 자연수이므로 그대로 return 

def solution(n):
    answer = 0
    for i in range(2, 1000000):
        if n % i == 1:
            answer = i
            return answer

print(solution(10)) # result 3
print(solution(12)) # result 11

