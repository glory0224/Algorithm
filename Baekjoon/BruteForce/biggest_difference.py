# 백준 10819번 차이를 최대로 
# https://sdesigner.tistory.com/51 코드

# Library 사용 풀이
 
from itertools import permutations
import sys
 
# 주어진 값 입력
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
 
# permutation 저장(per: reference of permutation tuples)
# 들어오는 배열의 모든 순서의 경우의 수를 튜플로 담는다.
per = permutations(a)
ans = 0


 
# 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    
    if s > ans:
        ans = s
        
 
    
print(ans)

# 라이브러리를 사용하지 않는 경우, 다음 순열의 풀이와 비슷하다.

# 나리야나 판디타의 다음 순열 알고리즘을 구현한 것 

import sys
 
 
def next_permutation(list_a):
    k = -1
    m = -1
 
    # 증가하는 마지막 부분을 가리키는 index k 찾기
    for i in range(len(list_a)-1):
        if list_a[i] < list_a[i+1]:
            k = i
 
    # 전체 내림차순일 경우, 반환
    if k == -1:
        return [-1]
 
    # index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
    for i in range(k, len(list_a)):
        if list_a[k] < list_a[i]:
            m = i
 
    # k와 m의 값 바꾸기
    list_a[k], list_a[m] = list_a[m], list_a[k]
 
    # k index 이후 오름차순 정렬
    list_a = list_a[:k+1] + sorted(list_a[k+1:])
    return list_a
 
 
# 주어진 값 입력 & 정렬
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
 
ans = 0
# 첫 순열 내 값 차이를 더해(s), ans 보다 크면 ans를 update
s = 0
for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s
 
arr = a
 
while True:
    arr = next_permutation(arr)
    if arr == [-1]:
        break
    s = 0
 
    # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
    for j in range(len(arr) - 1):
        s += abs(arr[j] - arr[j+1])
    if s > ans:
        ans = s
 
print(ans) 


