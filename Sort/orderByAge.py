# 백준 10814번 나이순 정렬 문제 

import sys

input = sys.stdin.readline

N = int(input())

member = []



for i in range(N):
    
    member.append(list(map(str, input().split())))

# 나이순으로 정렬(int) 
member.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(member[i][0], member[i][1])
