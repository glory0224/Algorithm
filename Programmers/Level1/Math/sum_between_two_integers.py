# 두 정수 사이의 합

# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.

def solution(a, b):
    answer = 0  
    
    if a < b:
        for num in range(a, b+1):
            answer += num   
    elif a > b:
        for num in range(a, b-1, -1):
            answer += num
    else:
        answer = a

    return answer

print(solution(3, 5)) # 12
print(solution(3, 3)) # 3
print(solution(5, 3)) # 12



