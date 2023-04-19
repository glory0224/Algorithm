# 문자열 계산하기

# my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

# 제한 사항

# 연산자는 +, -만 존재합니다. (하지만 나중에 문제에서 다른 연산자 경우의 수도 나올 수 있으므로 연산자 우선순위 범위를 늘려서 코드 작성)

# 문자열의 시작과 끝에는 공백이 없습니다.

# 0으로 시작하는 숫자는 주어지지 않습니다.

# 잘못된 수식은 주어지지 않습니다.

# 5 ≤ my_string의 길이 ≤ 100

# my_string을 계산한 결과값은 1 이상 100,000 이하입니다.
    # my_string의 중간 계산 값은 -100,000 이상 100,000 이하입니다.
    # 계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.
    # my_string에는 연산자가 적어도 하나 포함되어 있습니다.

# return type 은 정수형입니다.

# my_string의 숫자와 연산자는 공백 하나로 구분되어 있습니다.

# 입출력 예 #1

# 3 + 4 = 7을 return 합니다.


# def solution(my_string):
#     # 중위 표기식을 후위 표기식으로 변환 - a * b -> ab*
#     tokens = my_string.split()
#     operator_stack = [] # 연산자 저장 스택 선언(파이썬은 리스트가 스택)
#     output = [] # 연산할 숫자 저장
#     operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} # 연산자 우선순위 딕셔너리

#     for token in tokens:
#         if token.isnumeric(): # 문자열이 숫자인지 문자인지 판단
#             output.append(token)
#         elif token in operator_precedence: # 연산자 우선순위에 있는 경우
#             # \ 표시는 파이썬에서 코드가 길어 줄바꿈하는 문법
#             while operator_stack and operator_stack[-1] != '(' and \
#                 operator_precedence[token] <= operator_precedence.get(operator_stack[-1], 0):
#                     output.append(operator_stack.pop())
            
#             operator_stack.append(token)
        
#         # 토큰이 괄호인 경우
#         elif token == '(':
#              operator_stack.append(token)
#         elif token == ')':
#             while operator_stack and operator_stack[-1] != '(':
#                 output.append(operator_stack.pop())
#             if operator_stack and operator_stack[-1] == '(':
#                 operator_stack.pop()

#     # 연산자 스택의 연산이 남았다면 나머지 모두 추가
#     while operator_stack:
#         output.append(operator_stack.pop())    
        
#         # 후위 표기식을 계산하여 결과 반환
#         operand_stack = []
#         for token in output:
#             if token.isnumeric():
#                 operand_stack.append(int(token))
#             elif token in operator_precedence:
#                 operand2 = operand_stack.pop()
#                 operand1 = operand_stack.pop()
#                 if token == '+':
#                     result = operand1 + operand2
#                 elif token == '-':
#                     result = operand1 - operand2
#                 elif token == '*':
#                     result = operand1 * operand2
#                 elif token == '/':
#                     result = operand1 / operand2
#                 elif token == '^':
#                     result = operand1 ** operand2
#                 operand_stack.append(result)
#         return operand_stack.pop()



# 다른 풀이(훨씬 간결)

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))


print(solution("3 + 4"))            


            


        


