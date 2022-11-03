# 백준 10815번 숫자 카드 문제 
# 이진 탐색

"""
check의 요소들이 card에 존재 하는지 검사 

"""

import sys

input = sys.stdin.readline

N = int(input())

Sang = list(map(int, input().split()))

M = int(input())

Test = list(map(int, input().split()))

Sang.sort()

# 이진 탐색 함수 
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target: # 이분 탐색한 그 값이 비교 값과 같을 때 바로 반환
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 비교 값에 for문 돌면서 이진탐색 함수 호출
for i in range(M):
    if binary_search(Sang, Test[i], 0, N - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')