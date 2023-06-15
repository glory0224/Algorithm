# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    tmp = 0

    for i in range(n):
        tmp += x
        answer.append(tmp)
    
    return answer

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))