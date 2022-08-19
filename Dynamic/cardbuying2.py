#16194번 백준 카드 구매하기 2 최소값


N = int(input())
price = [0] + list(map(int, input().split()))

# 최소값을 구하는 문제로 min 함수를 사용해야 하기 때문에 0으로 초기화 하면 계속 0 값만 나옴 따라서 false로 초기화 
dp = [False for _ in range(N+1)]


for i in range(1, N+1):
    for k in range(1, i+1):
        if dp[i] == False:
            dp[i] = dp[i-k] + price[k]
        else:
            dp[i] = min(dp[i], dp[i-k] + price[k])

print(dp[i])

