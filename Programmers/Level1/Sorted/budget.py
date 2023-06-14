# 예산 문제 

# 처음에 dp 문제로 분류했으나 더 쉽게 풀이할 수 있는 정렬 방법이 존재했다.

# def find_max_length(nums, budget):
#     N = len(nums)
    
#     dp = [0] * (budget + 1)
    
#     for i in range(N):
#         num = nums[i]
        
#         for j in range(budget, num - 1, -1):
#             dp[j] = max(dp[j], dp[j - num] + 1)
    
#     return dp[budget]
    

# def solution(d, budget):
    
#     max_length = find_max_length(d, budget)
    
#     return max_length


def solution(d, budget):

    # 오름차순 정렬
    d_sorted = sorted(d)

    # 예산이 작은 부서부터 돈다.
    for idx, money in enumerate(d_sorted):
        # 이번 부서의 금액이 지원 가능하다면
        if money <= budget:
            budget -= money
        # 금액이 남지 않는 경우 그 전의 개수만 인정된다. -> 인덱스는 0부터 시작하기 때문에 현재 인덱스는 +1 된 상태 그대로 반환하면 이전의 개수와 동일
        else:
            return idx
    
    return len(d_sorted) # 전부 예산을 받는 경우 길이만큼 반환

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3], 10))