# 힙 자료구조 연습
# 더 맵게 

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
   
    heapq.heapify(scoville) # 추가 리스트 생성없이 힙 정렬

    print(scoville)

    cnt = 0
    
    while True:

        first = heapq.heappop(scoville) # 가장 작은 값 뽑음
        
        if first >= K: # K 이상 조건 만족 -> while 문 나감
            break

        if len(scoville) == 0:
            return -1

        second = heapq.heappop(scoville) # 두번째로 가장 작은 값

        heapq.heappush(scoville, first + (second * 2))
        print(scoville)
        cnt +=1
    
    
    
    return cnt

print(solution(scoville, K))




