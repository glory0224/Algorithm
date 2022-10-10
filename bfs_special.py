# 백준 16940번 bfs 스페셜 저지\

# https://recordofwonseok.tistory.com/362

#bfs 문제 풀이를 위한 라이브러리 
from collections import deque
import sys
input = sys.stdin.readline

# 시작 변수 
start = 1
N = int(input())
# 해당 그래프 크기만큼 2차원 배열 생성
graph = [[] for _ in range(N+1)]
# BFS 할때 방문 여부 확인을 위한 visited 변수 
visited = [-1 for _ in range(N+1)]
# 트리의 부모자식 관계를 알기 위한 변수
children = [set() for _ in range(N+1)]

# 연결된 간선에 따라 그래프를 생성한다.
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 올바른 순서인지 아닌지 비교할 탐색루트 입력 받기
test_case = list(map(int, input().split()))

# BFS
queue = deque()
queue.append(start)
visited[start] = 0
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1 # 방문을 하지 않았다면 방문처리한다.
            children[x].add(i) # x의 자식은 i이다. 
            queue.append(i)

# print(graph)
# print(children)            

# 현재 탐색중인 노드(i)의 자식 노드들이 어떤 인덱스 값부터 시작해야 하는지 저장하기 위한 변수 
next_index = 1

for i in test_case:
    # N의 길이와 같아진다면 leaf node들을 탐색하기 때문에 자식노드를 확인 하지 않아도 되서 종료한다.
    if next_index == N:
        break
    
    child_length = len(children[i]) # 자식의 길이 
    #print(child_length)
    c1 = set(test_case[next_index : next_index + child_length])
    c2 = children[i]
    #print("c1의 배열 : " , c1)
    #print("c2의 배열 : ", c2)
    if c1 != c2: # 비교 순서와 다른 경우 0 출력 후 즉시 함수 종료
        print(0)
        exit()
    next_index += child_length


print(1)
    