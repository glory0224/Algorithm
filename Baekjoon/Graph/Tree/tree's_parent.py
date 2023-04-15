# 백준 11725번 문제 트리의 부모 찾기 

import sys
input = sys.stdin.readline
# dfs 시간 초과 방지 
sys.setrecursionlimit(10**9)

N = int(input()) # 노드의 개수 
parents = [0 for _ in range(N + 1)] 
tree = [[] for _ in range(N + 1)]


for i in range(N-1):
    a , b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start, tree, parent):
    # 연결된 노드들부터 parents[i]의 부모가 없을 때 부모를 설정 해주고 DFS를 돌린다.
    for i in tree[start]: # 입력된 배열에서 값을 하나씩 뽑는다.
        if parent[i] == 0:
            parent[i] = start
            DFS(i, tree, parent)
            
DFS(1, tree, parents)

for i in range(2, N + 1):
    print(parents[i])

