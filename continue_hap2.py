# 백준 13398번 연속합 2

# A[i] = max(A[i], A[i-1] + A[i])
# dp를 사용하여 푼다.

import sys

input = sys.stdin.readline

T = int(input())

Arr = list(map(int, input().split()))

# 1. 특정 원소를 제거 하지 않는 경우 = 0
# 2. 특정 원소를 제거 하는 경우 = 1

# 2차원 dp 배열 생성 

dp = [[x for x in Arr] for _ in range(2)]

#print(dp) #[[10, -4, 3, 1, 5, 6, -35, 12, 21, -1], [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]] 

# T 가 1보다 큰 경우에 dp를 찾는다.

# 원소 제거 하지 않음 = dp[0][i] = max(dp[0][i-1] + Arr[i], dp[i]) 

# 원소 제거 = dp[1][i] = max(dp[0][i-1], dp[1][i-1] ++ Arr[i])

#  원소 제거 일 때는 다음의 두가지 사항중 큰 값을 대입

# - i번째 원소를 제거하는 경우 -> 위에서 구한 i - 1 번째 연속 합의 최대값을 그대로 대입

# - i번째 이전의 원소를 이미 제거하여 이전에 구해놓은 dp값에 현재 i 값을 더해주는 경우 -> i번째 이전의 원소를 제거한 연속합 값 + 현재 원소 i 값 

for i in range(1, T): 
   dp[0][i] = max(dp[0][i], dp[0][i-1] + Arr[i]) 
   dp[1][i] = max(dp[0][i-1], dp[1][i-1] + Arr[i])

#print(dp)
print(max(max(dp[0]), max(dp[1])))    


