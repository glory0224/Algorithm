# 6064번 백준 카잉 달력 문제 

# 시간 초과에 주의해서 코드를 작성해야한다. 

def num(m, n, x, y):
    while x <= m * n:
        # x에 계속 m 값이 더해지면서 만약 y를 뺐을 때 나머지가 0이면 그게 정답
        # EX) M = 10, N = 12, x = 3, y = 9
        # 1) 3%12 != 9%12
        # 2) 13%12 != 9%12
        # 3) 23%12 != 9%12
        # 4) 33%12 = 9%12 = 9
        if (x - y) % n == 0:
            return x
        x += m
    # m * n 값의 범위를 벗어났을 때도 해를 구하지 못한다면 유효한 표현이 아니기 때문에 -1 출력한다. 
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))
