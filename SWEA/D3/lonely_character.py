# 외로운 문자

# 스택을 활용한 문제

# 알파벳 소문자 만으로 이루어진 문자열이 주어진다.

# 이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.

# 같은 문자를 여러 번 짝지어서는 안 된다.

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.

# 이 문자열의 길이는 1이상 100이하이다.


# [출력]

# 각 테스트 케이스 마다 예제와 같은 형식으로 남는 문자를 사전 순서대로 출력한다.

# 만약 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.

# 입력
 	
# 6
# xxyyzz
# yc
# aaaab
# bca
# ppzqq
# qnwerrewmq

# 출력
# #1 Good
# #2 cy
# #3 b
# #4 abc
# #5 z
# #6 mn

T = int(input())

for tc in range(1, T+1):

    word = input()

    # 스택 선언
    stack = []

    # 반복문 돌면서 문자 하나씩 확인 이때 오름차순으로 정렬해줘서 스택에 오름차순으로 남아있도록 한다.
    for char in sorted(word):
        if stack and stack[-1] == char: # 스택이 비어있지 않고, 스택에 맨 마지막이 char와 같을 때
            stack.pop() # 해당 데이터를 빼서 삭제
        else:
            stack.append(char)
    
    # 스택에 남아있는 결과 문자열 형식으로 출력
    # 스택에 남아있는 결과가 없으면 Good 문자열 넣기
    result = ''.join(stack) if stack else "Good"

    print(f"#{tc} {result}")


