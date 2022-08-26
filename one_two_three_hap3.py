# 백준 15988번 1,2,3 더하기 3

import sys
input = sys.stdin.readline

# 1일 때 123 경우의 수, 2일 때 123 경우의 수 , 3일 때 123 경우의 수, 4일 때 123 경우의 수를 바로 dp에 초기화 
dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    # 4일때는 for문을 타지 않는다. 
    for j in range(len(dp), n):
        # print("j :" + str(j))
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])

