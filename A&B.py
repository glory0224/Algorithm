# 백준 12904번 A와 B 문제 
# https://chocochip101.tistory.com/entry/%EB%B0%B1%EC%A4%80-12904%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-A%EC%99%80-B
"""
아이디어 

S -> T 변경

- A연산 : 문자열 뒤에 A를 추가한다.
- B연산 : 문자열을 뒤집고 뒤에 B를 추가한다. 
 
- T의 마지막 문자가 A이면, A연산을 사용해서 T를 만듬
- T의 마지막 문자가 B이면, B연산을 사용해서 T를 만듬 

이 방법은 연산 횟수를 증가시켜 시간 복잡도가 높아진다. 

이를 반대의 관점에서 해석 

T -> S 변경 

- A연산 : 문자열 뒤에 A를 제거한다.
- B연산 : 문자열 뒤에 B를 제거하고 문자열을 뒤집는다.
 
"""

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

switch = False

while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        switch = True
        break
    
if switch:
    print(1)
else:
    print(0)
        