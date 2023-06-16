# 시저 암호

# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
# "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

def solution(s, n):
    # 소문자 나열
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    # 대문자 나열
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    answer = ''
    
    # 입력 받은 문자마다 n만큼 이동한 알파벳을 저장
    for char in s:
        if char == " ":
            answer += " " # 공백인 경우 공백 넣기
        # 소문자인 경우
        elif char in lower_alphabet:
            # n만큼 넘어간 위치의 알파벳을 반환하려면 길이가 넘어가는 경우 다시 0부터 시작할 수 있게 idx를 만들어야 한다.
            idx = (lower_alphabet.index(char) + n) % len(lower_alphabet)
            answer += lower_alphabet[idx]
        # 대문자인 경우
        elif char in upper_alphabet:
            idx = (upper_alphabet.index(char) + n) % len(upper_alphabet)
            answer += upper_alphabet[idx]
    
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))


            
            


