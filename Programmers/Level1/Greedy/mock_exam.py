# 모의고사 문제

def solution(answers):

    # 수포자 패턴 2차원 배열
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    # 수포자 스코어
    scores = [0,0,0]

    # 정답 확인 후 각 수포자가 맞힌 문제수 계산
    for i in range(len(answers)):
        # 수포자 패턴 길이만큼 반복
        for j in range(3):
            if answers[i] == patterns[j][i % len(patterns[j])]:
                scores[j] += 1
    
    # 가장 높은 점수의 수포자 점수를 찾는다.
    max_score = max(scores)

    # 높은 점수를 받는 사람이 여러명일 경우 오름차순 정렬
    winner = [i+1 for i in range(3) if scores[i] == max_score]

    return winner

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))