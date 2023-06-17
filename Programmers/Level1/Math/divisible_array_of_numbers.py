# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    
    for v in arr:
        if v % divisor == 0:
            answer.append(v)
    
    answer = sorted(answer)
    
    if answer:
        return answer
    else:
        answer.append(-1)
        return answer
    

