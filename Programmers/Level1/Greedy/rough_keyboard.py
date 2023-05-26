# 대충 만든 자판

# https://school.programmers.co.kr/learn/courses/30/lessons/160586

# 1. keymap 길이만큼 문자열을 돌면서 최소 인덱스를 뽑아서 저장한다.

# 2. keymap을 돌면서 같은 문자열이 있는 경우 min을 사용해서 최소 인덱스를 갱신한다.

# 3. 문자 일치 여부 확인 flag 변수 False로 선언하고 같은 문자열이 있는 경우 True로 변경

# 4. 문자가 일치 하지 않는 경우는 answer에 -1 추가

# 3. targets을 돌면서 keymap에 해당하는 문자가 있는 경우 cnt 변수에 더한다.

def solution(keymap, targets):
    answer = []

    
    # 비교할 target 문자 뽑기
    for target in targets:
        cnt = 0 # 자판을 몇번 누르는지에 대한 변수 초기화
        for t in target: # target 문자 뽑기
            min_value = float('inf') # 최소값 초기화
            found_char = False # 문자 확인 여부
            
            for k in keymap: # keymap 문자열 뽑기
                if t in k: # target 문자가 keymap 문자열 안에 있는지 확인
                    min_value = min(min_value, k.index(t)) # 최소값 비교
                    # 문자가 있으므로 flag 좌표 변경
                    found_char = True

            if not found_char: # 문자가 없는 경우
                answer.append(-1) # answer에 -1을 추가하고 종료
                break

            cnt += min_value + 1 # 누르는 횟수 갱신
        
        if found_char:  # 문자가 있는 경우에 대해서   
            answer.append(cnt) # 축적된 cnt 추가

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
print(solution(["AA"], ["B"]))
