# 콜라 문제

# def solution(a, b, n):
#     answer = 0
#     remain = 0
#     while n > 1:
#         if n % a == 0:
#             answer += n // a
#             n = n // a
#         else:
#             # 나머지 안마시고 교환이 안된 콜라
#             remain = n % a
#             n = n // a
#             answer += n 

#     if remain:
#         answer += 1

#     return answer

def solution(a, b, n):
    answer = 0
    # 보유 중인 빈 병이 a개 미만이면, 추가적으로 빈 병을 받을 순 없습니다.
    while not n < a:
        # 빈 병 a개를 가져다줄 때 새 콜라 묶음
        bundle = n // a
        # n -= bundle * a
        # 결국 n %= a 와 동일
        n %= a 
        # 콜라 b병을 주는 마트가 있을 때
        swap = bundle * b
        # print(swap)
        answer += swap
        n += swap # 새로 받은 콜라를 다시 n개 보충

    return answer


print(solution(2, 1, 20)) # result 19
print(solution(3, 1, 20)) # result 9