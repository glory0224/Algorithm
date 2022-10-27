# 백준 1202번 보석 도둑 문제 

'''
아이디어 
1. 각각의 가방에 들어갈 수 있는 가장 가격이 높은 보석을 조사
ex) 보석(무게, 가격) = (2, 99), (5, 65), (1, 23)
    가방 = 2, 10

2. 보석과 가방을 하나로 합치고 무게를 기준으로 오름차순 정렬

ex) (1,23), (2, 99) , 2, (5, 65) , 10

3. 가방을 검사해서 앞에 있는 보석 중에서 가장 가격이 큰 보석을 넣는다. 

4. 예시의 2의 경우 (2, 99)를 넣는다. 10은 (5,65)를 넣는다.

5. 무게가 증가하는 순으로 정렬했기 때문에, 앞의 모든 보석은 다 가방에 들어갈 수 있다. 

6. 보석의 경우에는 가격을 H 자료구조에 저장.. H 자료구조는 힙?
'''

import sys
import heapq # 힙 자료구조 

N, K = map(int, sys.stdin.readline().split())
jew = []
# 보석 저장
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))

# 가방 무게 저장
bags = []
for _ in range(K):
     bags.append(int(sys.stdin.readline()))

bags.sort()

answer = 0
tmp_jew = []

for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break

print(answer)

