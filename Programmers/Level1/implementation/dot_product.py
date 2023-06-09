# 내적

def solution(a, b):
    answer = 0

    for v1, v2 in zip(a, b):
        answer += v1 * v2
    
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))