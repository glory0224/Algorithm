# JadenCase 문자열 만들기

# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 처음 문제 풀이 (isdigit과 isalpha 함수 활용을 못함)

# def solution(s):
#     answer = ''
    
#     num = '0123456789'
    
#     s_list = s.split()
    
#     for word in s_list:
#         if word[0] not in num and word[0] != ' ':
#             answer += word[0].upper()
#             answer += word[1:].lower()
#         else:
#             answer += word
        
#         answer += ' '
    
#     answer = answer.rstrip()
            
#     return answer

# 다른 문제풀이 (flag 변수 이용)

def solution(s):
    answer = ""
    isFirst = True
    for char in s:
        # 1번째인 경우
        if isFirst:
            # 연속 공백이 나온 경우
            if char == " ":
                answer += char # 공백 더해줌
                isFirst = True # true로 그 다음 단어부터 조건에 제시된 처리하도록

            if char.isdigit(): # 숫자인 경우
                answer += char
                isFirst = False # flag 변경
            elif char.isalpha(): # 알파벳인 경우
                answer += char.upper() # 대문자 변경
                isFirst = False # flag 변경

        else: # 아닌 경우 나머지를 전부 소문자로 더한다.
            
            # 공백이 연속해서 나오는 조건이 있기 때문에 두번째가 공백인 경우 체크
            if char == " ":
                isFirst = True
            answer += char.lower()
    
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))

             
        
                

