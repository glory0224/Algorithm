# 스택/큐
# 기능개발

import math

def solution(progresses, speeds):

    answer = []

    remain_days = []

    for i in range(len(progresses)):

        days = math.ceil((100 - progresses[i]) / speeds[i])

        remain_days.append(days)

    
    # 작업 완료 횟수 및 이전 남은 작업 배포일 수 초기화
    cnt = 1
    before_day = remain_days[0]

    # 작업 완료 횟수 및 작업 배포일 계산

    for i in range(1, len(remain_days)):
        if remain_days[i] <= before_day:
            cnt += 1
        else: # 새로운 작업 배포일로 갱신
            answer.append(cnt) # 완료된 작업 기능의 개수(cnt)를 한번에 넣는다.
            cnt = 1 # 다시 완료 작업 cnt 1 초기화
            before_day = remain_days[i] # 남은 작업 배포일을 새로 갱신
            
    # 마지막 배포에 대한 처리가 필요하다.
    # 왜? 작업 배포일 계산 부분의 range 범위가 len 전까지이기 때문에 길이 직전까지만 돌기 때문에 마지막 배포 작업에 대한 처리는 빠져있기 때문이다. 
    answer.append(cnt)
    
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))

    

        
