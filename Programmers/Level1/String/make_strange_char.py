# 이상한 문자 만들기

# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

# 테스트 케이스는 통과, 하지만 전체 코드 통과 x

# 단어별로 리스트로 나누고 리스트별로 변환하여 처리

# def solution(s):
#     answer = ""
    
#     s_list = s.split()
    
#     for word in s_list:
#         for idx, char in enumerate(word):
#             if idx % 2:
#                 answer += char.lower()
#             else:
#                 answer += char.upper()
        
#         answer += " "
    
#     # 맨 마지막 공백도 추가되기 때문에 맨 마지막 공백 제거
#     answer = answer.rstrip()
                
#     # print(answer)
    
#     return answer

# 전체 테스트 통과 코드

# 입력된 문자열을 하나씩 처리

def solution(s):

    answer = ''

    idx = -1

    for char in s:
        # 공백인 경우 인덱스 -1
        if char == " ": 
            idx = -1
        else:
            idx += 1
            if idx % 2:
                answer += char.lower() # 홀수일 때 소문자
            else:
                answer += char.upper() # 짝수일 때 대문자
        
        if idx == -1: # 공백인경우 
            answer += " "
    
    return answer


print(solution("try hello world")) # "TrY HeLlO WoRlD"



