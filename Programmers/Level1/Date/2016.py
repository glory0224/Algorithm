# 2016년 문제

# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 

# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 

# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):

    answer = ''

    # 입력받은 연도의 1월 1일부터 입력받은 a월의 1월 1일까지의 날짜 계산
    days = b - 1

    for i in range(1, a): # 1월부터 a월까지
        if i == 2: # 윤년이기 때문에 += 29
            days += 29
        else:
            if i <=7: # 7월까지
                if i % 2 == 1: # 홀수 월은 31일
                    days += 31
                else: # 짝수 월은 30일
                    days += 30 
            else: # 8월부터
                if i % 2 == 1: # 홀수 월은 30일
                    days += 30
                else: # 짝수 월은 31일
                    days += 31
    

    # 총 날짜를 7일로 나눈 나머지에 해당하는 값에 따라 날짜 계산

    remainder = days % 7

    if remainder == 0: # 2016년의 1월 1일 요일은 금요일
        answer += 'FRI'
    elif remainder == 1:
        answer += 'SAT'
    elif remainder == 2:
        answer += 'SUN'
    elif remainder == 3:
        answer += 'MON'
    elif remainder == 4:
        answer += 'TUE'
    elif remainder == 5:
        answer += 'WED'
    elif remainder == 6:
        answer += 'THU'

    return answer


print(solution(5, 24)) # TUE





