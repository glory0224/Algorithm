# 기사단원의 무기

# 내 풀이 (시간 초과)

# def solution(number, limit, power):
#     answer = 0
    
#     divide_num_cnt = []
    
#     for num in range(1, number+1):
#         divide_num = []
        
#         for i in range(1, num+ 1):
#             if num % i == 0:
#                 divide_num.append(i)
    
#         divide_num_cnt.append(len(divide_num))
    
#     result = []
    
#     for j in range(len(divide_num_cnt)):
#         if divide_num_cnt[j] > limit:
#             result.append(power)
#         else:
#             result.append(divide_num_cnt[j])
    
#     answer = sum(result)
    
#     return answer


# 약수의 개수 구하기
def number_of_divisor(num):
    ans = 0
    div = 1 # 1부터 시작
    while div * div < num: # 나누려는 수의 제곱이 num의 범위를 넘어가면 종료 
        if num % div == 0: # 나누어 떨어지면
            ans += 2 # 나누는 수와 나눈 결과 두 개의 약수가 되므로 2개를 더해준다.
        
        div += 1 # 나누는 수를 1씩 증가
    
    # num이 div * div 범위를 초과하고 나누는 수의 제곱이 num과 같다면 완전 제곱수 
    if div * div == num: 
        ans += 1 # 추가 약수가 없기 때문에 1개 추가
    
    return ans



def solution(number, limit, power):
    
    answer = 0
    for knight_idx in range(1, number+1):
        # 자신의 약수의 개수에 해당하는 공격력을 가진다.
        atk = number_of_divisor(knight_idx)

        if atk > limit:
            answer += power
        else:
            answer += atk
    
    return answer



print(solution(5, 3, 2)) # result 10

print(solution(10, 3, 2)) # result 21