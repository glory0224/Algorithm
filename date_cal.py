# 백준 1476번 날짜 계산
import sys
input=sys.stdin.readline
# 입력 받을 3가지 수 
E, S, M = map(int, input().split())
# 1년부터 계속 세어주면서 주어진 수와 같아질 변수 
e, s, m = 1, 1, 1
# 세 수가 1씩 증가할 때마다 1년씩 증가할 변수 지정 
year = 1

while True:
    if e == E and s == S and m == M:
        print(year)
        break
    e += 1
    s += 1
    m += 1

    # 계속 더하다가 주어진 범위를 넘어가면 다시 1로 초기화 
    if e == 16: # 15 다음수 1 초기화 
        e = 1 
    if s == 29: # 28 다음수 1 초기화
        s = 1
    if m == 20: # 19 다음수 1 초기화
        m = 1
    year += 1




    
