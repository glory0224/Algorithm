# 과일 장수 문제

# def solution(k, m, score):
#     answer = 0

#     remain = len(score) % m

#     sorted_score = sorted(score)
    
#     # 나머지가 0과 0이 아닌 경우로 처리
#     # 이럴 경우 항상 최대 이익을 얻을 수 없음
#     # 반례로 m = 4 이고 sorted_score 길이가 7인 경우 슬라이싱 범위가 [4, 4, 4]로 잘못되어 최대 이익을 얻을 수 없습니다.
#     if remain == 0:
#         classified_score = [sorted_score[i:i+m] for i in range(0, len(sorted_score), m)]
#         for sublist in classified_score:
#             answer += min(sublist) * m 
    
#     else:
#         answer = min(sorted_score[-m:]) * m

#     return answer

def solution(k, m, score):
    answer = 0

    score.sort(reverse = True) # 내림차순 정렬

    # 점수의 길이가 박스 안의 개수보다는 커야함
    # while m <= len(score):
    #     # 박스에 넣을 수 있는 개수만큼 슬라이싱
    #     box = score[0:m]

    #     value = box[-1] * m
    #     answer += value

    #     score = score[m:] # 박스의 범위 다음부터 다시 슬라이싱하여 score의 범위 축소

    # (위의 계산 - 시간 초과 )
    
    # 내림차순 정렬한 박스 끝의 인덱스(제일 최소 값)의 점수에서 m 곱한 값을 더해주는 방식으로 변경
    for i in range(m-1, len(score), m):
        value = score[i] * m
        answer += value
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))