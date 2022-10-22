# 백준 11047번 동전 0 문제 

"""
1. 아이디어
- 동전을 저장한 뒤, 반대로 뒤집는다.
- 동전을 for 돌면서 동전 사용 개수 추가
- 동전을 사용한만큼 K값 갱신 

2. 시간 복잡도 
- O(N)

3. 자료구조 
- 동전 금액 : int []
- 동전 사용 cnt : int
- 남은 금액 : int

"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [ int(input()) for _ in range(N)]

# 제일 큰 값부터 나눠주어야 최소 값이 나온다는 증명을 토대로 그리디 알고리즘 사용 
# 따라서 오름차순 정렬되어 있는 것을 내림차순으로 변경한다. 
coins.reverse()

# 나눈 횟수 
cnt = 0

for each_coin in coins:
    # 가치의 합의 몫 cnt 저장 
    cnt += K // each_coin
    # 가치의 합의 나머지를 갱신 
    K = K % each_coin


print(cnt)
