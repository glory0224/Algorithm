# 최장 공통 부분 수열 문제

# dp 풀이

# 주어진 두 문자열의 최대 공통 부분 수열(Longest Common Sequence)의 길이를 계산하는 프로그램을 작성하시오.

# 예를 들어 "acaykp"와 "capcak"의 경우, 두 문자열의 최대 공통 부분 수열은 "acak"로 길이가 4이다.

# 최장 공통 부분문자열(Longest Common Substring)을 계산하는 것이 아님에 주의한다.

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫째 줄에 두 문자열이 공백을 사이에 두고 주어진다.

# 각 문자열은 알파벳 소문자로만 구성되어 있음이 보장된다.

# 각 문자열의 길이는 1,000 이하의 자연수이다.

# [출력]

# 각 테스트 케이스마다 ‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 공통 부분 수열의 길이를 출력한다.

# 입력
# 1
# acaykp capcak

# 출력
# #1 4

# 공통 부분을 찾아내고 공통 부분이 있다면 dp 테이블을 생성하여 + 1 다르다면 이전에 dp 테이블에 있던 길이 값 중에 제일 큰 값을 최장 길이로 갱신

def find_common_substring(A, B):
    # 각 문자열의 길이
    len_A = len(A)
    len_B = len(B)

    # A 크기 * B 크기만큼 dp 테이블 생성
    dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

    # 문자열 길이만큼 2중 반복 돌면서 같은 문자가 있는지 확인
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            # 만약 현재 문자가 같다면 dp 테이블 길이 +1
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # 같지 않다면 이전 dp 테이블 중 최대 길이를 현재 dp 테이블에 추가
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[len_A][len_B] # 가장 긴 길이의 dp 값 반환(최장 길이)





T = int(input())

for tc in range(1, T+1):

    A, B = input().split()

    # 공통 부분 수열 길이 찾는 함수
    result = find_common_substring(A, B)

    print(f"#{tc} {result}")