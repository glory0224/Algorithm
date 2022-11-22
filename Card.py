# 백준 11652번 카드 문제 

# '입력되는 카드값을 특정 리스트에 정리한 뒤 나중에 제일 많은 값을 출력하면 되겠다.'

# 딕셔너리를 사용하여 문제 풀기
# 이유는 key 값에 카드의 번호를 저장하고, value값에 카드의 개수를 저장하여 마지막에 value 값을 내림차순 해주고 같다면 key 값을 오름차순 해주기 위해서

import sys 

input = sys.stdin.readline

N = int(input())

card_dic = {}

for i in range(N):
    card = int(input())
    if card in card_dic:
        card_dic[card] +=1
    else:
        card_dic[card] = 1


# card_dic.items() : 해당 딕셔너리 Key와 Value를 쌍으로 얻는다.
result = sorted(card_dic.items(), key= lambda x: (-x[1], x[0])) # 개수를 기준으로 내림차순 

print(result[0][0])