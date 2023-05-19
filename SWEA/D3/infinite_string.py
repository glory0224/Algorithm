# 무한 문자열 문제

# 문자열 S에 대해, f(S)를 S를 무한히 반복해서 얻은 문자열이라고 정의하자. 예를 들어 f(“abcd”) = “abcdabcdabcdabcd…” 이다.


# S≠T이라도 f(S)=f(T) 일 수 있다. 예를 들어 S = “ababab”, T = “abab”라면 f(S)와 f(T) 모두 “ababababababab…”이다.

# 두 개의 문자열 S와 T가 주어질 때, f(S)=f(T)인지의 여부를 구하는 프로그램을 작성하라.

 

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

 

# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 두 개의 문자열 S와 T가 공백 하나를 사이로 두고 주어진다. S와 T는 알파벳 소문자(a-z)로만 구성되어 있으며, 1글자 이상 50글자 이하이다.

 

# [출력]

# 각 테스트 케이스마다, f(S)=f(T)라면 ‘yes’를, f(S)≠f(T)라면 ‘no’를 출력한다.

# 단순 길이 제한으로 반복하는 문제인줄 알았는데, 최대공약수와 최소공배수를 활용한 무한 길이 문자열 비교 문제

# 입력
# 3
# ababab abab
# aba bab
# hello hello

# 출력
# #1 yes
# #2 no
# #3 yes

import math

T = int(input())

for tc in range(1, T+1):
    a, b  = map(str, input().split())

    # 문자열의 길이 측정
    len_a = len(a)
    len_b = len(b)

    # 길이의 최소 공배수 구하기  - 두 문자열의 길이 곱 // 두 수의 최대공약수
    lcm = len_a * len_b // math.gcd(len_a, len_b)

    new_a = (a * (lcm // len_a))[:lcm] # f(S) 생성 # f(S)는 S를 무한히 얻은 것이기 때문에 50으로 제한하는 것이 아닌 a, b 문자열의 길이의 최소 공배수 길이만큼으로 제한 
    new_b = (b * (lcm // len_b))[:lcm] # f(T) 생성

    if new_a == new_b:
        print(f"#{tc} yes")
    else:
        print(f"#{tc} no")

