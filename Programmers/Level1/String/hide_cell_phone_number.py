# 핸드폰 번호 가리기

# 마지막 4자리 빼고 전부 '*'로 채우는 문제 

def solution(phone_number):
    answer = ''

    last = phone_number[-4:] # 마지막 4자리 
    remain = phone_number[:-4] # 그 외 자리
    protect = '' # '*' 채울 변수 

    for i in range(len(remain)):
        protect += '*'
    
    answer = protect + last

    return answer