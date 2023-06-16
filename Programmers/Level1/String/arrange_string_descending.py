# 문자열을 내림차순 배치

# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.

# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):

    answer = ''

    upper_lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    s_index = [] # s의 인덱스 배열

    for char in s:
        idx = upper_lower.index(char)
        s_index.append(idx)

    s_index = sorted(s_index, reverse=True)

    for i in range(len(s_index)):
        answer += upper_lower[s_index[i]]
    
    return answer


print(solution("Zbcdefg")) # "gfedcbZ"
