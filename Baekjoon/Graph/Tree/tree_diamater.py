# 백준 1967번 트리의 지름
# https://velog.io/@coding_egg/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# bfs를 두번 이용해서 지름 구하는 방식

from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

# print(graph)

def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0 # 시작 할 때만 값을 방문 처리 0으로 초기화 
    _max = [0, 0]
    
    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                # print("visit[" + str(e) + "]" + str(visit[e]))
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e
                    # print(_max)
    
    return _max


dis, node = bfs(1) # 1번 인덱스부터 탐색, bfs로 한 정점에서 모든 정점을 탐색하여 가장 먼 거리를 구한다.
# print(node)
dis, node = bfs(node) # 가장 먼 거리의 노드부터 모든 정점을 다시 bfs 해주면 결과적으로 트리의 지름을 구할 수 있다. 
print(dis)
