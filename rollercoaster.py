# 백준 2873번 롤러코스터 문제 
# 그리디 알고리즘 
# https://seungyong20.tistory.com/39

"""
    최선의 해를 찾기 위해 경우의 수마다 코드를 다르게 짠다. 
    
    1. r(행)이 홀수인 경우 ㄹ 모양으로 방문한다면 모든 칸을 방문 할 수 있다. 
    
    2. c(열)이 홀수인 경우 ㄹ 모양을 90도 꺾은 형태로 방문한다면 모든 칸을 방문 할 수 있다. 
    
    3. r, c가 짝수인 경우 
    
    r과 c가 모두 짝수인 경우는 무조건 1칸을 제외하고 이동해야한다. 이 칸을 어떻게 제외 할 것인지가 문제의 핵심 

"""

import sys

r, c = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

if r % 2 == 1:
    # 3*3 기준으로 아래 프린트를 하면 RRDLLDRR
    print(('R' * (c - 1) + 'D' + 'L' * (c -1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1:
    print(('D' * (r - 1) + 'R' + 'U' * (r -1) + 'R') * (c // 2) + 'D' * (r -1))
# r, c가 짝수인 경우 모든칸을 방문 할 수 없기 때문에 무조건 1칸을 제외함
# 이때 1칸 제외는 일정한 패턴이 있음 -> 이 부분을 피해서 이동해야한다. 
elif r % 2 == 0 and c % 2 == 0:
    # 문제에서 최대 기쁨을 1000으로 주었기 때문에 
    low = 1000 
    position = [-1, -1]
    
    for i in range(r):
        # 짝수의 행일 경우 
        if i % 2 == 0:
            # 홀수의 칸만 지정한다. 
            for j in range(1, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j] # 제일 작은 값으로 계속 초기화 
                    position = [i, j]
        # 홀수 행이라면 
        else:
            # 짝수 칸만 지정
            for j in range(0, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j] # 제일 작은 값으로 계속 초기화 
                    position = [i, j]
           
    # 제외할 칸의 x(열) 기준 // 2를 해서 이동해준다.          
    res = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
    # 홀수를 짝수로 만든다.
    # ex) 2 * (5 // 2) = 4
    x = 2 * (position[1] // 2)
    # y는 무조건 위에서 시작하기 때문에 0
    y = 0
    # 홀수를 짝수로 만들어준 다음 무조건 오른쪽 1칸을 이동해야하는 과정이 있기 때문에 
    # xbound에 +1 해서 넣는다. 
    xbound = 2 * (position[1] // 2) + 1
    
    # x와 xbound가 같거나 y가 맨 밑까지 갔다면 종료 
    while x != xbound or y != r - 1:
        # x가 xbound보다 왼쪽에 있고 [y, xbound] 와 position의 값이 틀리다면 오른쪽 이동
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        # x가 xbound랑 값이 같으며, [y, xbound]와 position의 값이 틀리다면 왼쪽 이동
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += 'L'
        # 마지막 줄이 아니라면 아래쪽으로 이동 
        if y != r - 1:
            y += 1
            res += 'D' 
    
    # 이동해야 하는 나머지 칸 // 2  -> 지금의 짝수 예제에서는 0 도출      
    res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)
    
    print(res)

