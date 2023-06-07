# 없는 숫자 더하기

def solution(numbers):
    answer = 0
    oneTonine = [1,2,3,4,5,6,7,8,9]
    
    for num in oneTonine:
        if num not in numbers:
            answer += num
            
    return answer

print(solution([1,2,3,4,6,7,8,0])) # result 5 + 9 = 14
print(solution([5,8,4,0,6,7,9])) # result 1 + 2 + 3 = 6

