# 백준 12919번 A와 B 2
# 그리디 알고리즘
# DFS 알고리즘 

# A와 B 문제의 핵심과 유사 

# S를 T로 변환하는 문제이지만 사용되는 경우의 수가 너무 많아 시간이 너무 오래걸려서 
# 역으로 T에서 S를 만드는 접근으로 해결한다. 
# 파이썬의 슬라이싱과 dfs를 사용해서 해결 


import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

# print(T[1:][::-1])

def dfs(T):
    if T == S: # 종료 조건
        print(1)
        sys.exit()
    
    if len(T) == 0: # 배열에 비교 값이 없으면 0 반환
        return 0
    
    if T[-1] == 'A': # 마지막이 A이면 
        dfs(T[:-1]) # 제거한 뒤 재귀
    
    if T[0] == 'B': # 처음이 B이면 
        dfs(T[1:][::-1]) # B 제거하고, 뒤집어서 재귀 

dfs(T)
print(0)