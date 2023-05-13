# 새샘이의 7 - 3 - 5 게임

# 숫자게임을 좋아하는 새샘이는 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.

# 이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 각 정수는 1이상 100이하이다.

 
# [출력]

# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.

# 입력
# 2
# 1 2 3 4 5 6 7
# 5 24 99 76 1 77 6

# 출력
# #1 14
# #2 181

# 최악의 반복되는 경우도 7^3 = 343번 반복이므로 3중 for문을 돌면서 단순 반복으로 문제 풀이 가능

for tc in range(int(input())):
    num_list = list(map(int, input().split()))

    answer = []

    # 3중 for문을 돌면서 모든 수의 경우를 다 더한다.

    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
               answer.append(num_list[i] + num_list[j] + num_list[k])

    # 중복 제거
    answer = list(set(answer))

    # 오름차순 정렬
    answer.sort(reverse=True)

    # 5번째 수 출력
    print(f"#{tc+1} {answer[4]}")

    

