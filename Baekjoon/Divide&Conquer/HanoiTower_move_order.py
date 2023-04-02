# 백준 11729번 하노이 탑 이동 순서 

n = int(input())


def solve(n, x, y):
    if n == 0:
        return
    solve(n-1, x, 6-x-y)
    print(x, y)
    solve(n-1, 6-x-y, y)

# 맨위의 숫자 카운트를 어떻게 세어주는지 고민했는데 답은 간단했다. 그냥 계산해서 print 해주고 시작한다.
print(2**n-1)    
solve(n, 1, 3)
