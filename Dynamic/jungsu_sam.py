# 백준 1932번 정수 삼각형 문제 
# https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python - 코드 

T = int(input())

# dp[i][j] = i행 j열이 선택되었을 때, 최대 합 

dp = []

for i in range(T):
    dp.append(list(map(int, input().split())))         


for i in range(1,T) :                           ## 행을 기준으로 for문 구성
    for j in range(0,i+1) :                     ## 열을 기준으로 for문 구성
        if j == 0 :
            dp[i][0] += dp[i-1][0]              # 0열끼리 더하기(트리 구조로 내려갈 때 맨 왼쪽)
        elif j == i :
            dp[i][j] += dp[i-1][j-1]            # 마지막 열끼리 더하기 (트리 구조로 내려갈 때 맨 왼쪽)
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])    # 두 화살표중 더 큰 경우 받아들이기(맨 왼쪽과 맨 오른쪽을 제외한 경우)

print(max(dp[T-1]))   # T-1행에서의 최댓값 출력 -> 왜? 인덱스가 0부터 시작하기 때문에 dp 최대 값은 T 입력 값에 -1 한 배열에 저장된다. 

