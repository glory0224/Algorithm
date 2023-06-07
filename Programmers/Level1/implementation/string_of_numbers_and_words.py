# 숫자 문자열과 영단어

# 문자열 처리와 매핑을 통한 구현 방식

def solution(s):
    # 정답 문자열
    answer = ""

    # 문자 타입의 영어로 된 숫자 매핑할 딕셔너리 선언
    num_dict = {
        "zero" : 0,
        "one" : 1, 
        "two" : 2, 
        "three" : 3, 
        "four" : 4,
        "five" : 5, 
        "six" : 6, 
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    # 문자 타입의 숫자를 비교할 리스트 선언
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 문자 하나씩 확인할 변수 선언
    keyword = "" 

    for char in s:
        keyword += char
        # keyword 가 딕셔너리에 존재하면 (영어인 경우)
        if keyword in num_dict:
            answer += str(num_dict[keyword]) # 해당 키워드의 값 넣고
            keyword = "" # 키워드 초기화
        elif keyword in num_list: # 문자가 숫자인 경우
            answer += keyword
            keyword = ""
        
    
    return int(answer) # 정수형으로 형변환

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
