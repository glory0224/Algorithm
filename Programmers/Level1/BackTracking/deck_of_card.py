# 카드 뭉치 문제

# 코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.

# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.

# 한 번 사용한 카드는 다시 사용할 수 없습니다.

# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.

# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

# 예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.

# 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.


# 문제 접근 : 카드는 순서대로 한장씩 사용 (순열), 한 번 사용한 카드는 다시 사용 x(중복없음) - 조합, 순열 문제에 사용되는 재귀함수와 백트래킹 방식 선택

# 문제의 시간복잡도 : O(N!) - 가능한 모든 조합을 탐색


def solution(cards1, cards2, goal):
    answer = ''

    def is_possible(cards1, cards2, goal):
        
        # 인덱스가 계속 하나씩 증가하므로 나중에는 리스트의 길이가 0
        # 종료 조건
        if len(goal) == 0:
            return True
        
        # cards1 에서 goal의 시작 단어가 있는 경우
        # cards1의 첫번째 인덱스와 goal의 첫번째 인덱스가 같고 길이가 0보다 길면 값이 존재하면서 문제의 조건 시작이 완성
        if len(cards1) > 0 and cards1[0] == goal[0]: 
            if is_possible(cards1[1:], cards2, goal[1:]): # 함수를 재귀방식으로 호출, 다음 is_possible의 0번 인덱스 비교는 이전 cards1[1] 인덱스부터 시작 - 계속해서 goal과 cards1이 하나씩 인덱스가 밀리면서 비교된다. 
                return True
        
        # cards2에서 goal의 시작 단어가 있는 경우 
        # cards1과 동일하게 백트레킹으로 비교
        if len(cards2) > 0 and cards2[0] == goal[0]:
            if is_possible(cards1, cards2[1:], goal[1:]):
                return True
        
        return False


    # Yes 와 No를 판단하는 함수
    if is_possible(cards1, cards2, goal):
        answer += 'Yes'
    else:
        answer += 'No'
    
    
    return answer




print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))