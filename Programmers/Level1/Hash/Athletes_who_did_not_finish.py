# 완주하지 못한 선수

# 해시 테이블 이용(dict)

def solution(participant, completion):

    dict = {}

    # 참가한 선수들이 있다면 dictionary에 + 1
    for x in participant:
        dict[x] = dict.get(x, 0) + 1 # get으로 키와 값에 해당하는 딕셔너리 원소를 생성하고 그 값에 + 1
    
    print(dict)

    # 완주한 선수들이 있다면 해당 dictionary에 -1
    for x in completion:
        dict[x] -= 1
    
    # 완주하지 못한 선수
    not_complete = [k for k, v in dict.items() if v > 0]

    return not_complete


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # result  "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # result "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # result "mislav"