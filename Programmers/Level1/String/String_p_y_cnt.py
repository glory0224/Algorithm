# 문자열 내 p와 y의 개수

# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 

# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 

# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

def solution(s):
    
    lower_char = {"p" : 0 , "y" : 0}
    upper_char = {"P" : 0, "Y" : 0}
    
    for char in s:
        if char in lower_char:
            lower_char[char] += 1
        elif char in upper_char:
            upper_char[char] += 1
    
    # print("lower_char : ", lower_char)
    # print("upper_char : ", upper_char)
    
    if (lower_char["p"] + upper_char["P"]) == (lower_char["y"] + upper_char['Y']):
        return True
    elif (lower_char["p"] + upper_char["P"]) != (lower_char["y"] + upper_char['Y']):
        return False
    else:
        return True
    
print(solution("pPoooyY")) # true
print(solution("Pyy")) # false