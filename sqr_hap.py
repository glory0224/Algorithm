# 백준 1699번 제곱수의 합 
# 풀이 참조 https://jyeonnyang2.tistory.com/50

T = int(input())
# i는 제곱수의 합, dp[i]는 필요한 항의 최소 개수 1 ~ n까지 초기화함
dp = [i for i in range(T+1)]

for i in range(1, T+1):
    for j in range(1,i):
        # j는 1부터 i-1까지의 수 중 제곱한 값이 i보다 크지 않아야 한다.
        if j*j > i:
            break 
        if dp[i] > dp[i-j*j] + 1: # +1의 의미 -> 2*2의 경우의 수를 더해줘야 하기 때문에 매번마다 +1을 해준다. 
            dp[i] = dp[i-j*j] + 1
        
print(dp[T])
