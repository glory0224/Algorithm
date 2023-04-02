# 백준 11651번 좌표 정렬하기 2

import sys

input = sys.stdin.readline

N = int(input())

coordinate = []

for i in range(N):
    coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x: (x[1],x[0]))

for i in coordinate:
    print(i[0], i[1])
