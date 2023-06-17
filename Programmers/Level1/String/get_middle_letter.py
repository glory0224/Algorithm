# 가운데 글자 가져오기

def solution(s):
    answer = ''
    
    # print("홀수 가운데 확인 : ", s[len(s)//2])
    # print("짝수 가운데 확인 : ", s[len(s)//2-1:(len(s)//2)+1])
    
    if len(s) % 2 ==0:
        answer += s[(len(s)//2)-1:(len(s)//2)+1]
    else:
        answer += s[len(s)//2]
    
    return answer

print(solution("abcde"))
print(solution("qwer"))
