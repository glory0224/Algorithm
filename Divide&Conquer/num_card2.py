# 백준 10816번 숫자카드2 숫자카드1 유형과 비슷한 문제
# 상한과 하한의 개념 
# 이분 탐색 개념뿐만 아니라 다양한 풀이를 해주신 블로거님 공유 
# https://chancoding.tistory.com/45

from sys import stdin


_ = stdin.readline()
Sang = sorted(map(int, input().split()))


_ = stdin.readline()
Test = map(int, input().split())

cnt = 0

def binary_search(card, Sang, start, end):
   
    if start > end:
        return 0
    mid = (start + end) // 2
    if card == Sang[mid]:
        return Sang[start:end+1].count(card)
    elif card < Sang[mid]:
        return binary_search(card, Sang, start, mid - 1)
    else:
        return binary_search(card, Sang, mid+1, end)
    
card_dic = {}

for card in Sang:
    start = 0
    end = len(Sang) - 1
    if card not in card_dic:
        card_dic[card] = binary_search(card, Sang, start, end)
        
print(' '.join(str(card_dic[x]) if x in card_dic else '0' for x in Test))


