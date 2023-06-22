# 영어 끝말잇기

# 반복문과 set 자료구조를 이용한 문제 풀이

# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 이전에 등장했던 단어는 사용할 수 없습니다.
# 한 글자인 단어는 인정되지 않습니다.

# 제한 사항
# 끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
# words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
# 단어의 길이는 2 이상 50 이하입니다.
# 모든 단어는 알파벳 소문자로만 이루어져 있습니다.
# 끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
# 정답은 [ 번호, 차례 ] 형태로 return 해주세요.
# 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

def solution(n, words):
    # 이전에 등장했던 단어는 사용할 수 없습니다. - set 함수 사용
    used = set()

    # 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
    for i in range(len(words)):
        # 반복될 유저 번호 수
        userNum = (i % n) + 1
        # 반복된 회차
        turn = (i // n) + 1

        # 이전에 등장했던 단어는 사용할 수 없습니다.
        # 한 글자인 단어는 인정되지 않습니다.
        if 1 < len(words[i]) and words[i] not in used:
            if i == 0: # 처음 시작인 경우 해당 단어가 중복되지 않도록 set에 넣는다.
                used.add(words[i])
            elif words[i-1][-1] == words[i][0]: # 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
                used.add(words[i])
            else: # 앞선 두 조건에 해당하지 못해서 걸린 경우 그 때 틀린 사람 번호와 순서를 반환
                return [userNum, turn]
        else:
            return [userNum , turn] # 이전의 등장했거나 한 글자인 경우 바로 반환
    
    # 아무도 끝말잇기의 규칙을 어기지 않고 끝난 경우
    return [0,0]



print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3, 3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1, 3]
