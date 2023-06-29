# 연속 부분 수열 합의 개수

# 철호는 수열을 가지고 놀기 좋아합니다. 
# 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 
# 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 
# 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.
# 원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
# 원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

# 부분 수열 1, 2 로 나눠서 개수를 구하는 경우
# def solution(elements):
#     #[7,9,1,1,4] 전체 합
#     total_sum = sum(elements)
#     # 길이가 5인 경우의 합을 set함수에 넣고 시작
#     partial_sum = {total_sum}

#     # 순환되지 않는 경우의 부분 수열의 합으로 부분 수열 1을 구한다.
#     for s in range(len(elements)): # 시작
#         for e in range(s+1, len(elements)):
#             # [9, 1]
#             partial_sum1 = sum(elements[s:e])
#             # 7]    [1, 4 = [7,9,1,1,4] - [9, 1] 
#             partial_sum2 = total_sum - partial_sum1
#             print("partial_sum1 : ", partial_sum1)
#             print("partial_sum2 : ", partial_sum2)
#             partial_sum.add(partial_sum1)
#             partial_sum.add(partial_sum2)

#     return len(partial_sum)


# 한칸씩 왼쪽으로 이동하면서 각 배열을 더해준 값을 set 함수에 넣어서 길이 반환
    # [7, 9, 1, 1, 4] 길이가 1
    # [9, 1, 1, 4, 7] 길이가 2
    # [1, 1, 4, 7, 9] 길이가 3
    # [1, 4, 7, 9, 1] 길이가 4
    # [4, 7, 9, 1, 1] 길이가 5


def solution(elements):
    offset = 1 # 길이가 1인 경우
    curr_sums = elements[:] # 배열 복사(옮기면서 더해주는 기준 배열)
    partial_sums = set(curr_sums) # 길이 1에 해당하는 부분 수열 합 저장

    # offset이 elements의 길이를 초과하면 종료
    while offset < len(elements):
        for i in range(len(elements)):
            # 기준 배열의 각 값에 offset 만큼 이동한 값을 더해준다. 
            # [7, 9, 1, 1, 4] + [9, 1, 1, 4, 7] = [16, 10, 2, 5, 11]
            curr_sums[i] += elements[(i+offset) % len(elements)]
            partial_sums.add(curr_sums[i]) # 중복되지 않는 set에 넣는다.

        offset += 1 # 길이를 증가시킨다.

    return len(partial_sums) # 개수 반환
            
print(solution([7,9,1,1,4]))