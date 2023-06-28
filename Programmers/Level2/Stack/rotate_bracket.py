# 괄호 회전하기 문제

# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
# 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

# 문제의 핵심은 왼쪽으로 한칸씩 이동했을때 괄호가 올바르게 닫혀있는지 확인하는 문제

def is_valid(s):

    # stack 자료구조 이용해서 괄호가 닫혔는지 여부 확인
    stack = []

    # s의 문자를 하나씩 뽑으면서 확인
    for char in s:
        # 만약 스택에 존재하고 들어간 값이 괄호의 시작이고 뽑힌 char가 괄호를 닫는 문자라면
        if stack and stack[-1] == '(' and char == ')':
            stack.pop()
        elif stack and stack[-1] == '{' and char == '}':
            stack.pop()
        elif stack and stack[-1] == '[' and char == ']':
            stack.pop()
        else: # 해당되지 않는다면 stack에 문자열을 채운다.
            stack.append(char)

    return stack == [] # stack이 비워있다면 괄호가 제대로 열고 닫힌 것으로 True 아니라면 False


def solution(s):
    answer = 0
    
    # 왼쪽으로 이동하는 방법
    # 맨 앞에 값을 맨 뒤로 넘긴다. (인덱스 이용)
    for i in range(len(s)):
        # 넘기면서 괄호가 제대로 닫혔는지 확인
        if is_valid(s[i:] + s[:i]): # 인덱스를 활용해서 왼쪽으로 이동시키면서 넘기는 이 부분 중요
            answer += 1 # 닫힌 케이스 추가
    return answer

print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0