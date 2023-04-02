# 백준 11053번 
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    
    # 중요 포인트! 위의 if문에서 true인 값이 나올 때만 dp[i] + 1 적용, 아닐 경우 여기를 타지 않고 j의 다음 인덱스로 넘어감
    dp[i] += 1
    
print(max(dp))
