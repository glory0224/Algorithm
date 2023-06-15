# 하샤드 수

def is_harshad(x):
    str_x = str(x)

    digit_hap = 0 # 자리수 합

    for char in str_x:
        digit_hap += int(char)
    
    if x % digit_hap == 0: # 나누어 떨어지는 경우
        return True
    else:
        return False # 아닌경우

    

def solution(x):

    answer = is_harshad(x)

    return answer


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))