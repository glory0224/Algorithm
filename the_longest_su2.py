# 백준 12015번 가장 긴 증가하는 부분 수열 2

# 가장 긴 증가하는 부분 수열 3과 동일한 코드

from bisect import bisect_left

input()
A = list(map(int, input().split()))

dp = []

for i in A:
    k = bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
        
print(len(dp))