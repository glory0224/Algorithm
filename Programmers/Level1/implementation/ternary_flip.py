# 3진법 뒤집기

def solution(n):

    answer = 0
    ternary = '' # 3진법 표현 저장 변수

    # n을 3진법으로 변환
    while n > 0:
        # print("n : ", n)
        remainder = n % 3
        # print("remainder : ", remainder)
        # print("ternary : ", ternary)
        ternary = str(remainder) + ternary
        n = n // 3
    
    # 3진법을 역순으로 뒤집기
    rev_num = ternary[::-1]

    answer = int(rev_num, 3) # 문자열 rev_num을 3진법 변환 -> 10진수 변환

    return answer

print(solution(45))
print(solution(125))