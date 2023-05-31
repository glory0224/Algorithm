# 명예의 전당 1

# def solution(k, score):
#     answer = []
    
#     honor = []
    
#     #  매일 1명의 가수가 노래를 부르고, 시청자들의 문자 투표수로 가수에게 점수를 부여합니다.
#     for i in range(len(score)):
#         # 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다.
#         if i+1 > k:

#             s_honor = sorted(honor, reverse=True)
#             max_val = max(s_honor[0], score[i])
            
#             if max_val > s_honor[0]:
#                 s_honor.insert(0, max_val)

#             if score[i] < min(honor):
#                 s_honor.remove(min(s_honor))

#             print(s_honor)

#             answer.append(min(s_honor))
#             print("k일 다음 answer : ", answer)

#         else:
#             honor.append(score[i])
#             answer.append(min(honor))
#             print("k일까지 answer : ", answer)
            
#     return answer

# 처음 풀이보다 훨씬 더 간단한게 접근 가능

# min, max 사용 없이도 충분히 풀어낸다.

def solution(k, scores):
    
    answer = []

    hall_of_fame = []

    for score in scores:
        hall_of_fame.append(score)
        hall_of_fame.sort(reverse=True)
        # k의 범위만큼 자른다.
        hall_of_fame = hall_of_fame[:k]
        # 마지막 범위를 추가한다. 
        answer.append(hall_of_fame[-1])

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))