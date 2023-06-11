# 실패율

# 정렬을 통한 구현

# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):

    # 참가자 수
    challengers = len(stages)

    # 각 스테이지별 실패율 딕셔너리
    failure_rate_dict = {n+1:0 for n in range(N)}

    # 스테이지까지 반복
    for stage in range(1, N+1):
        # 시작 스테이지가 입력 받은 스테이지에 있는 경우
        if stage in stages:
            # 해당 스테이지 수
            stage_cnt = stages.count(stage)
            # 실패율 계산
            failure_rate = stage_cnt / challengers
            # 실패율 딕셔너리 저장
            failure_rate_dict[stage] = failure_rate

            # 다음 스테이지로 넘어가기전 현재 스테이지만 도달한 수를 전체 참가자 수에서 빼준다.
            challengers -= stage_cnt
    

    # 실패율이 높은 스테이지 순으로 내림차순, 실패율이 동일한 경우 스테이지 순으로 내림차순 정렬
    sorted_list = sorted(failure_rate_dict.items(), key=lambda x: (-x[1], x[0]))

    # print(sorted_list)

    # [(스테이지, 실패율)] 순으로 정렬된 리스트에서 스테이지만 뽑아서 다시 리스트로 생성
    answer = [x[0] for x in sorted_list]

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))