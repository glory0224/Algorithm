# [Professional] 합

# 연속된 정수의 합 중 최대값 구하는 문제 - 부분 수열의 합 중 최대 값 - dp 활용

# N개의 정수가 입력으로 주어진다.

# 이때 연속하여 몇 개의 정수를 골라 합을 구할 수 있다.

# 예를 들어, 1 3 -8 18 -8 이 있다고 하자.

# 그럼 2번부터 4번까지의 수를 골라 합을 구하면, 3+(-8)+18 = 13이다. 

# 이렇게 연속해서 정수를 골라 합을 구할 때, 그 합의 최대가 몇인지 구하는 프로그램을 작성하세요.

# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)

# 각 테스트 케이스 첫째 줄에 숫자 N이 주어진다. (3 ≤ N ≤ 100,000)

# 둘째 줄에는 절대값이 1000이하의 정수 N개가 공백을 사이에 두고 입력된다.

# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 연속된 정수의 합의 최대값을 출력하시오.

# 입력
# 1
# 5
# 1 3 -8 18 -8

# 출력
# #1 18

def find_max_value(nums):
    # dp 테이블 생성
    dp = [0] * len(nums)

    # 최대값 초기화
    max_value = 0

    # 초기값 설정 - 초기 값을 설정하는 이유는 for 문에서 max 함수로 비교할 전의 인덱스가 필요하기 때문
    dp[0] = nums[0]

    for i in range(len(nums)):
        # max 함수로 비교
        dp[i] = max(nums[i], dp[i-1] + nums[i]) # 이전 dp 테이블과 현재 숫자를 더한 값과 그냥 현재 숫자를 Max 비교한다. 
        max_value = max(max_value, dp[i]) # max_value로 담겨 있던 값과 dp[i]로 새로 생성된 max_value 중 크기 비교

    return max_value

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    nums = list(map(int, input().split()))

    max_value = find_max_value(nums)

    print(f"#{tc} {max_value}")

