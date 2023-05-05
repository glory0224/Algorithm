# 부분 수열의 합 - DP 방식 사용

# A1, A2, ... , AN의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 2개의 자연수 N(1 ≤ N ≤ 20)과 K(1 ≤ K ≤ 1000)가 주어진다.

# 두 번째 줄에는 N개의 자연수 수열 A가 주어진다. 수열의 원소인 N개의 자연수는 공백을 사이에 두고 주어지며, 1 이상 100 이하임이 보장된다.


# [출력]

# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.

# 입력
# 1
# 4 3
# 1 2 1 2

# 출력
# #1 4

def find_hap(seq, k):
    n = len(seq)

    dp = [0] * (k+1)

    dp[0] = 1 # 0의 경우는 경우의 수 1개

    for i in range(n):
        # k부터 역순으로 dp를 호출해야 이전 dp를 호출하지 않는다.
        for j in range(k, seq[i] - 1, -1):
            dp[j] += dp[j - seq[i]]

    return dp[k]


T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    answer = find_hap(seq, k)

    print(f"#{tc} {answer}")

