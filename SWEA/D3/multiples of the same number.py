# 숫자가 같은 배수

# 자연수 N이 있다. N의 10진법 표기(단, 0으로 시작하지 않도록 표기해야 함)에서 나타나는 숫자들을 재배열하여 N보다 큰 N의 배수(즉 2N, 3N, …, k•N, …) 를 만들 수 있는지 판단하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 자연수 N (1 ≤N ≤ 106) 이 공백 하나를 사이로 두고 주어진다.
 

# [출력]
# 각 테스트 케이스마다, 주어진 자연수에 나타난 숫자들을 재배열하여 더 큰 배수를 만들 수 있다면 ‘possible’, 불가능하다면 ‘impossible’을 출력한다.

# 입력
# 3
# 142857
# 1
# 1035

# 출력
# #1 possible
# #2 impossible
# #3 possible

T = int(input())

for tc in range(1, T+1):

    N = input().strip()

    # 만약 N의 첫자리가 0인경우 재배열해도 배수를 만들 수 없기 때문에 바로 impossible 출력 후 다음 테스트 케이스 진행
    if N[0] == '0':
        print(f"#{tc} impossible")

    # '0'부터 '9'에 해당하는 딕셔너리 생성
    counts = {str(d):0 for d in range(10)}

    # N의 각 자리숫자 확인하며 counts 딕셔너리 해당 자리 값을 1씩 증가
    for digit in N:
        counts[digit] += 1

    # 가능 불가능 flag 변수 선언
    is_possible = False

    # 재배열하면서 N보다 큰 N의 배수를 만들기 위해 2 ~ 9에 해당하는 k를 N에 곱해주고 이를 candidate 변수에 문자열로 저장
    for k in range(2, 10):
        candidate = str(k * int(N))
        candidate_count = {str(d):0 for d in range(10)}

        # N과 k*N의 자리수가 다르다면 이는 재배열하여 N보다 큰 N의 배수를 만들 수 없는 경우
        # 다음 테스트 케이스 진행
        if len(candidate) != len(N):
            continue

        # k*N의 케이스의 자리수에 해당하는 값 증가
        for digit in candidate:
            candidate_count[digit] += 1

        # 원래 수와 k배수를 곱한 값의 모든 자리에서 같은 숫자들로 이루어져 있다면, 재배열 하여 N보다 큰 N의 배수로 만들 수 있는 경우
        # 이 경우에는 flag 변수를 True로 변경하고 종료
        if candidate_count == counts:
            is_possible = True
            break

    if is_possible:
        print(f"#{tc} possible")
    else:
        print(f"#{tc} impossible")