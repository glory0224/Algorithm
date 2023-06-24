# 구명 보트 문제

# 문제는 통과하지만 

# 3 5 6 2 8 8 8 8 8 8 8 과 같은 무게 배열이 있을 때

# 시간 복잡도가 linear time(선형 시간)만큼 증가하기 때문에 효율성 측면에서 떨어짐(시간 초과 발생)

# from bisect import bisect_right

# def solution(people, limit):
#     # 오름차순 정렬
#     people = sorted(people)
#     # 구명 보트 개수 
#     boat = 0
#     while people:
#         # 제일 무거운 무게
#         heavy = people.pop(-1)
#         light_idx = bisect_right(people, limit-heavy)
#         print("light_idx : ", light_idx)
#         print("people :", people)
#         if 0 < light_idx: # 인덱스가 0 이상인 경우 
#             people.pop(light_idx - 1)
#         boat += 1
#     return boat


# 시간 초과가 발생하지 않게 코드를 작성 

# from bisect import bisect_right

# def solution(people, limit):
#     # 각 무게 횟수 딕셔너리 생성
#     weightCount = dict()

#     # people 무게를 딕셔너리에 담는다.
#     for w in people:
#         if w in weightCount:
#             weightCount[w] += 1
#         else:
#             weightCount[w] = 1
    
#     weights = sorted(list(set(people))) # 어떤 키 값이 남아 있는지 확인용 리스트를 정렬한 상태로 선언 

#     boat = 0
#     print(boat, weightCount, weights)

#     while weights:
#         Heavyweight = weights[-1] # 제일 큰 무게
#         HeavyCount = weightCount[Heavyweight] # 그 무게의 등장 횟수

#         if HeavyCount == 1:
#             weights.pop(-1)
        
#         LightweightIdx = bisect_right(weights, limit - Heavyweight) # bisect 함수로 같이 탈 수 있는 무게 인덱스 반환

#         if 0< LightweightIdx: # 같이 탈 수 있는 친구가 있는 경우 
#             Lightweight = weights[LightweightIdx - 1]
#             LightCount = weightCount[Lightweight]

#             if Heavyweight == Lightweight: # 같이 탈 수 있는 친구의 무게가 동일한 경우
#                 boat += HeavyCount // 2

#                 weightCount[Heavyweight] = HeavyCount % 2
#                 if weightCount[Heavyweight] == 0 and Heavyweight in weights:
#                     weights.remove(Heavyweight)
            
#             else: # 같이 탈 수 있는 친구의 무게가 다른 경우 
#                 boat += min(HeavyCount, LightCount)

#                 weightCount[Heavyweight] -= min(HeavyCount, LightCount) # 보트를 타고 나간 사람만큼 제거
#                 # 해당 명수가 0명이면 제거
#                 if weightCount[Heavyweight] == 0 and Heavyweight in weights:
#                     weights.remove(Heavyweight)
                
#                 weightCount[Lightweight] -= min(HeavyCount, LightCount)
#                 if weightCount[Lightweight] == 0 and Lightweight in weights:
#                     weights.remove(Lightweight)
        
#         else: # 같이 탈 수 있는 무게가 없는 경우
#             boat += HeavyCount

#             weightCount[Heavyweight] -= HeavyCount
#             if weightCount[Heavyweight] == 0 and Heavyweight in weights:
#                 weights.remove(Heavyweight)
        
#         print(boat, weightCount, weights)
#     return boat


# 더 간결한 코드로 작성하기

def solution(people, limit):
    answer = 0
    # L        H
    people.sort() # 정렬
    Lidx, Hidx = 0, len(people) - 1 # 가장 가벼운 무게, 가장 무거운 무게로 나눈다.

    while Lidx < Hidx: # 무게 인덱스가 서로 교차되면 while 종료
        # 2명이 타고 나가는 경우 (H + L)
        # 몸무게가 제일 무거운 친구와 제일 가벼운 친구의 합이 limit 안에 있는 경우 탄다.
        if people[Lidx] + people[Hidx] <= limit:
            Lidx += 1
            Hidx -= 1
        # 아닌 경우라면 오름차순 정렬되어 있기 때문에 그 다음 값은 당연히 같이 타고 못나간다.
        # Hidx를 내려주면서 Lidx와 타고 갈 수 있는지만 검사
        else:
            Hidx -= 1
        
        answer += 1
    
    if Hidx == Lidx: # 만약 숫자가 가운데에서 뭉쳐있는 경우 혼자 타고 나오기 때문에 + 1
        answer += 1
    return answer




print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))