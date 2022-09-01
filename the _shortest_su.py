# 백준 11722번 가장 긴 감소하는 부분 수열
import sys

T = int(input())

A = [int(x) for x in sys.stdin.readline().split()]

# 가장 긴 감소하는 부분 수열의 길이 저장
dp = [1 for i in range(T)]

for i in range(T):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))