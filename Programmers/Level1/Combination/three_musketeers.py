# 삼총사 문제

# 조합 문제로 재귀함수로 문제풀이

# def find_zero_sum(nums):
#     cnt = 0

#     # 조합에 대한 백트레킹 함수 선언
#     def backtracking(combination, start): # 조합 배열, 시작 인덱스를 매개변수로 하는 함수
#         # UnboundLocalError: cannot access local variable 'cnt' where it is not associated with a value
#         # 지역변수가 아님을 선언해주지 않으면 위의 에러가 발생한다.
#         nonlocal cnt 
#         if len(combination) == 3: # 3개 숫자가 채워진 경우
#             if sum(combination) == 0: # 3개 숫자의 합이 0인 경우
#                 cnt += 1 # 정답 개수 추가
#             return

#         for i in range(start, len(nums)): # 시작 인덱스부터 nums 길이까지 for문 돌면서 재귀 함수 호출

#             backtracking(combination + [nums[i]], i+1) # 조합에 nums[i] 값 추가하면서 인덱스 증가
    
#     backtracking([], 0) # 백트레킹 호출
#     return cnt
        

# def solution(numbers):
#     answer = 0

#     answer = find_zero_sum(numbers)

#     return answer

# 비슷한 풀이 방식 추가

def recursion(numbers, summed, count):
    if count == 3: # 종료 조건
        if summed == 0: 
            return 1
        else:
            return 0
    else: # 3개가 안되는 경우
        three = 0 # 재귀함수의 결과 값이 저장될 변수
        for i in range(len(numbers)):
            three += recursion(numbers[i+1:], summed + numbers[i], count + 1) # 현재 인덱스 값 다음을 넘기고, summed 에 더해간다.
        return three  

def solution(numbers):
    # 인덱스의 위치 확인
    # print(numbers)
    # for i in range(len(numbers)):
    #     print(i, numbers[:i], numbers[i], numbers[i:])
    
    return recursion(numbers, 0, 0)

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))