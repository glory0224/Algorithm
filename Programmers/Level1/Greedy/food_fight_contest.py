# 푸드 파이트 대회

def solution(food):
    answer = ''
    
    for idx, val in enumerate(food):
        mod = val // 2
        rev_answer = ''
        # 음식의 순서를 음식의 양만큼 반복해서 추가
        for _ in range(mod):
            answer += str(idx)
        
    rev_answer = answer[::-1]
    answer += '0'
    answer += rev_answer

    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
