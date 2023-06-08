# 신규 아이디 추천

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# 처음 코드 (일부 테스트 케이스 통과 못함)

# def solution(new_id):
#     capital_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     small_letter = "abcdefghijklmnopqrstuvwxyz"
#     special = "~!@#$%^&*()=+[{]}:?,<>/"
#     answer = ''
#     prev_char = ""

    
#     for char in new_id:
#         # 대문자를 대응되는 소문자로 치환
#         if char in capital_letter:
#             answer += small_letter[capital_letter.index(char)]
#         # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
#         elif char in special:
#             continue
#         # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#         elif char == '.' and prev_char == '.':
#             continue
#         else:
#             answer += char
#             prev_char = char

#     # 마침표가 처음이나 끝에 위치한다면 제거
#     if answer.startswith('.'):
#         answer = answer[1:]
#     if answer.endswith('.'):
#         answer = answer[:-1]

#     # 빈 문자열이라면, new_id에 "a"를 대입합니다.
#     if len(answer) == 0:
#         answer += 'a'
    
#     # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
#     if len(answer) >= 16:
#         answer = answer[:15]
#         # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
#         if answer.startswith('.'):
#             answer = answer[1:]
#         if answer.endswith('.'):
#             answer = answer[:-1]
    
#     # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
#     if len(answer) <= 2:
#         while len(answer) !=3:
#             answer += answer[-1]

#     return answer

# 조금 더 간결한 코드 (문제 풀이 통과)

def solution(new_id):
    special = "~!@#$%^&*()=+[{]}:?,<>/"
    answer = ""

    # 1단계 대문자를 소문자로 변환
    new_id = new_id.lower()

    # 2단계 특수문자 제거
    for char in new_id:
        if char.isalnum() or char in '-_.':
            answer += char
    
    # 3단계 연속된 마침표 하나로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계 처음이나 끝에 위치한 마침표 제거
    answer = answer.strip('.')

    # 5단계 빈 문자열이면 'a' 대입
    if not answer:
        answer = 'a'
    
    # 6단계 길이가 16자 이상이면 15자로 제한, 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    
    # 7단계 길이가 2자 이하이면 길이가 3이 될때까지 마지막 문자 추가
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm")) # result "bat.y.abcdefghi"
print(solution("z-+.^.")) # result "z--"
print(solution("=.=")) # result "aaa"
print(solution("123_.def")) # result "123_.def"
print(solution("abcdefghijklmn.p")) # result "abcdefghijklmn"