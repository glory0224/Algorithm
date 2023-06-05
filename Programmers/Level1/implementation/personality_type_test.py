# 성격 유형 검사

def solution(survey, choices):
    answer = ''
    
    # 각 유형의 지표 점수 딕셔너리
    mbti1 = {'R' : 0, 'C' : 0, 'J' : 0, 'A' : 0}
    mbti2 = {'T' : 0, 'F' : 0, 'M' : 0, 'N' : 0}
    
    # 선택 점수
    choice_point = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    for s, c in zip(survey, choices):
        if s[0] in mbti1 and c <= 3:
            mbti1[s[0]] += choice_point[c]
        elif s[0] in mbti2 and c <= 3:
            mbti2[s[0]] += choice_point[c]
        elif s[1] in mbti1 and c >= 5:
            mbti1[s[1]] += choice_point[c]
        elif s[1] in mbti2 and c >= 5:
            mbti2[s[1]] += choice_point[c]
        else:
            continue # 4번을 선택한 경우 점수를 세지 않는다. 

    # mbti1, mbti2 의 딕셔너리 값을 각각 비교하고 큰 값의 키를 answer에 더한다. 이때 값이 동일하면 사전순으로 빠른 키를 더함
    for key1, key2 in zip(mbti1.keys(), mbti2.keys()):
        if mbti1[key1] > mbti2[key2]:
            answer += key1
        elif mbti1[key1] < mbti2[key2]:
            answer += key2
        elif mbti1[key1] == mbti2[key2]:
            # 같은 경우 사전순으로 더 빠른 key를 answer에 삽입
            if key1 < key2:
                answer += key1
            else:
                answer += key2

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) # "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3])) # "RCJA"