# 백준 2751번 수 정렬하기 2

import sys

input = sys.stdin.readline

N = int(input())
result = []

for i in range(N):
    result.append(int(input()))

result.sort()

for i in result:
    print(i)
