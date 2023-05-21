# 달리기 경주

# 얀에서는 매년 달리기 경주가 열립니다. 
# 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
# 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
# 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

# # 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 

# # 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

# 제한사항
# 5 ≤ players의 길이 ≤ 50,000
# players[i]는 i번째 선수의 이름을 의미합니다.
# players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
# players에는 중복된 값이 들어가 있지 않습니다.
# 3 ≤ players[i]의 길이 ≤ 10
# 2 ≤ callings의 길이 ≤ 1,000,000
# callings는 players의 원소들로만 이루어져 있습니다.
# 경주 진행중 1등인 선수의 이름은 불리지 않습니다.

# 딕셔너리를 활용하여 시간 초과를 방지한 그리디 알고리즘 풀이 방식

# 딕셔너리를 2개 사용하는 방식은 시간 복잡도를 고려하여 선택한 방법입니다. 이를 통해 호출에 대한 처리를 더 효율적으로 수행할 수 있습니다.

# 첫 번째 딕셔너리는 선수의 이름을 키(key)로 하고 등수를 값(value)으로 하는 딕셔너리입니다. 이를 통해 선수의 이름을 기반으로 빠르게 등수를 찾을 수 있습니다.

# 두 번째 딕셔너리는 등수를 키(key)로 하고 선수의 이름을 값(value)으로 하는 딕셔너리입니다. 이를 통해 등수를 기반으로 빠르게 선수의 이름을 찾을 수 있습니다.

# 따라서, 호출이 발생할 때마다 딕셔너리를 순회하지 않고 효율적으로 등수와 선수의 이름을 관리하여 선수들의 순서를 업데이트할 수 있습니다. 이를 통해 시간 복잡도를 개선할 수 있습니다.

# 1. {선수 : 등수}, {등수: 선수 } 두 딕셔너리 변수를 지정한다.

# 2. calling을 반복문으로 돌며 지정된 선수의 이름을 기반으로 calling 선수(i)의 딕셔너리 값들을 한 등수를 올려 수정하고
# calling 선수(i)의 앞 등수 선수를 한 등수 내려 수정해준다.

# 3. return은 선수의 이름을 return idx 딕셔너리의 vlaue 값을 list 형식으로 return 

def solution(players, callings):

    idx = {i : player for i , player in enumerate(players)} # 등수 : 선수 딕셔너리 
    player = {player : i for i, player in enumerate(players)} # 선수 : 등수

    # 이름 순서대로 확인
    for calling in callings:
        loc = player[calling] # 현재 등수 
        loc2 = loc - 1 # 앞의 등수
        calling2 = idx[loc2] # 앞의 선수 이름

        idx[loc] = calling2 # 현재 등수에 앞의 등수 선수 이름 넣기
        idx[loc2] = calling # 앞의 등수의 현재 등수 선수 이름 넣기

        player[calling] = loc2 # 현재 이름 불린 플레이어는 앞의 등수로
        player[calling2] = loc # 앞 선수 이름은 현재 등수로

    return list(idx.values())






