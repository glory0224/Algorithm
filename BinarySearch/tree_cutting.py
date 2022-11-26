# 백준 2805번 나무 자르기
# https://claude-u.tistory.com/446 
# pypy3 문제 제출

import sys

input = sys.stdin.readline

myTree, needTree = map(int, input().split())

Tree = list(map(int, input().split()))

start, end = 1, max(Tree)

while start <= end:
    mid = (start + end) // 2
    treeNum = 0
    for i in Tree:
        if i >= mid:
            treeNum += i - mid # 기준점인 i를 기준으로 남는 값을 더해준다.
    if treeNum >= needTree:
        start = mid + 1
    else:
        end = mid - 1

print(end)
