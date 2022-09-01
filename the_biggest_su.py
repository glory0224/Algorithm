# 11055번 가장 큰 증가 부분 수열 

import sys

T = int(input())

# A = list(map(int, input().split()))

# 위의 방법으로 만들 수도 있지만 아래와 같은 방법으로도 리스트를 만들 수 있다. 
A = [int(x) for x in sys.stdin.readline().split()]

#dp = [0 for i in range(T)]

# A배열의 모든 값들을 리스트 형태로 저장한다. 
dp = A[:]
 
#    0   1   2   3   4   5   6   7   8   9
# A  1  100  2  50  60   3   5   6   7   8 
# dp 1  100  2  50  60   3   5   6   7   8 

# i가 j보다 클 때 값을 비교해준다. 
for i in range(T):
    for j in range(i): 
        if A[i] > A[j]:  
          dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))            

# dp 1  101  3  53  113.. max = 113

 


