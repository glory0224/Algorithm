# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    # 최고와 최저 순위 담을 변수
    answer = []
    # 0이 모두 당첨번호와 동일한 경우의 최대 번호 개수
    max_same = []
    # 0dl 모두 당첨번호와 동일하지 않은 경우 최소 번호 개수
    min_same = []

    # 로또 맞춘 개수별 순위 딕셔너리
    lotto_cnt = {
        6 : 1, 
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }

    # 내가 뽑은 로또 번호 순회
    for num in lottos:
        if num in win_nums:
            min_same.append(num)
            max_same.append(num)
        elif num == 0:
            max_same.append(num)
    
    # 최고 순위와 최저 순위 순서대로 answer에 삽입
    answer.append(lotto_cnt[len(max_same)])
    answer.append(lotto_cnt[len(min_same)])

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # result [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # result [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
