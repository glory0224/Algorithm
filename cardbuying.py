# 11052번 백준 카드 구매하기 문제 

N = int(input())
p = [0] + list(map(int, input().split())) # 0을 붙여주지 않으면 아래 for문에서 list index out of range 오류 발생

dp = [0 for _ in range(N+1)]

# print(dp[0])
# print(p)




for i in range(1,N+1):
    for k in range(1, i+1): # p의 index가 0부터 4까지인데 range가 1부터 시작하기때문에 index는 5 따라서 out of index 에러 발생
        dp[i] = max(dp[i], dp[i-k] + p[k])

print(dp[i])