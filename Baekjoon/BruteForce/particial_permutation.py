#백준 1182번 부분 수열의 합 
# 조합 패키지 사용?
# 비트마스크로 어떻게 풀지?

# https://seongonion.tistory.com/98

# 조합 패키지 사용해서 푼 풀이 

from itertools import combinations
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1):
    comb = combinations(arr, i)

    # 모든 조합을 돌면서 합이 s와 같으면 cnt로 출력 
    for j in comb:
        # print(j)
        if sum(j) == s:
            # print("조합의 합 : " + str(sum(j)))
            cnt += 1

print(cnt)
