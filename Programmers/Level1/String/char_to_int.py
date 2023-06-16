# 문자열을 정수로 바꾸기

# str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

def solution(s):
    answer = 0
    
    print(int(s[1:]))
    
    
    if s[0] == "-":
        answer = int(s[1:]) * -1
    else:
        answer = int(s)
        
    
    return answer

