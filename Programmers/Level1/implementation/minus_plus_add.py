# 음양 더하기 문제

def solution(absolutes, signs):
    
    answer = 0
    
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
            
    return answer

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))