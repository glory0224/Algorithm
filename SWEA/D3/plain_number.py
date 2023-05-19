# 평범한 번호 문제

# 1 이상 N 이하의 정수가 적혀 있는 길이 N의 순열 p1, p2, …, pN이 있다. 수열에 있는 모든 숫자는 서로 다르다. 2 ≤ i ≤ N-1이며, pi-1, pi, pi+1 중 pi가 최솟값도, 최댓값도 아니라면 pi를 평범한 숫자라고 정의한다. 주어진 순열에서 평범한 숫자의 개수는 몇 개인가?

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
#     ∙ 첫 번째 줄에 정수 N 이 주어진다. (3 ≤ N ≤ 20)
#     ∙ 이후 N개의 정수 pi가 주어진다. (3 ≤ pi ≤ N) 모든 pi는 서로 다르다.

# [출력]
# 각 테스트 케이스마다 정답을 출력하라.

# 입력
# 2
# 3
# 1 3 2
# 5
# 1 3 5 4 2

# 출력
# #1 0
# #2 2

# 배열의 인덱스를 활용할 줄 아는지 묻는 문제

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    num_list = list(map(int, input().split()))

    answer = 0

    # 배열을 돌면서 앞 뒤의 인덱스를 확인해야 하기 때문에 1부터 N - 1까지 
    for i in range(1, N - 1):
        # 최대값 확인
        max_num = max(num_list[i-1], num_list[i], num_list[i+1])

        # 최소값 확인
        min_num = max(num_list[i-1], num_list[i], num_list[i+1])

        # 만약 숫자가 max_num과 min_num이 아닌 경우 평범한 숫자이기에 +1
        if num_list[i] != max_num and num_list[i] != min_num:
            answer += 1
    
    print(f"#{tc} {answer}")
    

