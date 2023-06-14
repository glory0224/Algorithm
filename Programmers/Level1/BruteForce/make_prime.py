# 소수 만들기

# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수 구하기

# nums의 중복 없음

# 3개 수를 각각 더해주는 경우의 수


# 배열의 크기가 작고 소수 판별이 자주 일어나지 않는 경우 효율적인 코드

# import math

# def find_three_sums(nums):

#     N = len(nums)

#     # 결과를 담을 배열
#     result = []

#     # 3중 for문으로 모든 경우의 수를 구한다.
#     for i in range(N - 2):
#         for j in range(i+1, N-1):
#             for k in range(j+1, N):
#                 result.append(nums[i] + nums[j] + nums[k])
    
#     # 리스트 반환
#     return result
                
# def is_prime(num):

#     if num < 2:
#         return False

    
#     for i in range(2, int(math.sqrt(num)) + 1):
#             # 2부터 num의 제곱근까지 나누어 떨어지는 수가 있다면 소수 아님
#         if num % i == 0:
#             return False
    
#     return True


# def solution(nums):

#     answer = 0

#     # nums 리스트에서 3개의 수로 만들 수 있는 조합 리스트 반환
#     num_list = find_three_sums(nums)

#     for num in num_list:
#         # 소수 판별 후 answer + 1
#         if is_prime(num):
#             answer += 1
        
#     return answer


# 배열의 크기가 크고, 소수 판별이 상대적으로 자주 발생하는 경우 이 코드가 효율적이다. 

def recursion(nums, depth, added, res_dict):
    if depth == 3:
        # 지금까지 더한 결과값이 딕셔너리에 존재한다면 
        if added in res_dict:
            res_dict[added] += 1
        else:
            res_dict[added] = 1 # 그 경우의 수 카운트
    
    else:
        for idx in range(len(nums)):
            # 소모한 현재 idx에서 +1 한 배열, 단계 +1, 현재 idx 값을 added에 더한 값, 정답 딕셔너리를 함께 넘긴다.
            recursion(nums[idx+1:], depth+1, added + nums[idx], res_dict)

        
def solution(nums):

    # added: 경우의 수
    num_count = dict()

    recursion(nums, 0, 0, num_count)

    print(num_count)

    # 어떤 수들이 소수인지
    # 딕셔너리 안에 있는 수 중에 제일 큰 수까지는 소수 판별을 하고자 범위를 max로 지정
    is_prime = [1 for _ in range(max(num_count)+1)]
    print(is_prime) # 딕셔너리의 최대 키 값에 해당하는 수 만큼 1이 채워진다.
    is_prime[0], is_prime[1] = 0, 0 # 0과 1은 소수에 해당하지 않으므로 0으로 변경

    answer = 0

    for num in range(2, max(num_count)+1):
        # 자신이 소수라면
        if is_prime[num] == 1:
            # 소수를 만들 수 있는 경우
            if num in num_count:
                answer += num_count[num] # 해당 경우의 수 모두 기록
            mul = 2
            while num * mul < max(num_count)+1:
                is_prime[num * mul] = 0 # 해당 수의 곱은 소수가 아님
                mul += 1 # 무한 루프가 걸리지 않게 mul을 계속 증가
        # 자신이 소수가 아님
        else:
            pass
    
    return answer


print(solution([1,2,3,4])) # result 1
print(solution([1,2,7,6,4])) # result 4