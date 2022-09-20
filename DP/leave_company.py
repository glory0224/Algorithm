# 백준 14501번 퇴사 

# https://pacific-ocean.tistory.com/199
# dp 방식을 이용

N = int(input())
T = []
P = []
dp = []

for i in range(N):
    t , p = map(int, input().split())
    T.append(t)
    P.append(p)
    dp.append(p)
dp.append(0)

for i in range(N-1, -1, -1):
    # 일수를 넘어가면 어차피 퇴사이기 때문에 값만 넘겨준다. 
    if T[i] + i > N:
        dp[i] = dp[i +1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
        
print(dp[0])

