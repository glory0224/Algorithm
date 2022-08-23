# 백준 14002번 

T = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(T)]

for i in range(T):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            longA = A[i]
            dp[i] = dp[j]
            
    
    dp[i] += 1

print(max(dp))

longA = [] # 가장 긴 수열 증가 배열 
order = max(dp) # dp 저장 변수 


# T -1 : 인덱스 0부터 세어주기 위해서 
# -1 : 인덱스를 5부터 역으로 for문 돌려주기 위해서 
# -1 : 인덱스를 하나씩 차감
for i in range(T -1, -1, -1):
    # dp 배열의 max값과 같음 = 가장 긴 증가하는 부분 수열
    if dp[i] == order: 
        longA.append(A[i]) # 새로운 배열에 넣는다. 
        # 최대 길이의 경우의 수가 없어졌기 때문에 그 다음으로 해당하는 order값을 1씩 감소 시켜가면서 A 배열과 비교한다. 
        order -= 1

longA.reverse() # 역순으로 배열이 저장되었기 때문에 정답과 같은 출력을 하기 위해 reverse 함수 사용 

print(*longA) # 파이썬에서 배열 출력할 때 허용되는 형식 *