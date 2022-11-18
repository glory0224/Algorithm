# 백준 11650번 좌표 정렬하기 

import sys

input = sys.stdin.readline

N = int(input())
coordinate = []

for i in range(N):
    coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x: (x[0],x[1])) # 람다 방식으로 정렬

for i in coordinate:
    print(i[0], i[1])
