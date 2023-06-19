# 올바른 괄호

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

def solution(s):

    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: #  # 처음부터 ")" 가 등장한 경우 괄호가 성립 안되기 때문에 false
                return False
        
    if stack: # 스택에 괄호가 남아있는 경우 성립이 안된 것이기 때문에 false
        return False
    else: # 스택에 괄호가 남아있지 않다면 모두 성립된 것이기 때문에 True
        return True
    

print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False

