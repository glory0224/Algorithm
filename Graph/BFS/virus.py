# 백준 2606번 바이러스 문제 (bfs 풀이)

# https://bio-info.tistory.com/152

from collections import deque

n=int(input()) # 컴퓨터 개수 입력
v=int(input()) # 연결선 개수 입력

graph = [[] for i in range(n + 1)] # 그래프 초기화
visited = [0]*(n+1) # 방문한 컴퓨터인지 표시

for i in range(v): # 그래프 생성
    a,b = map(int, input().split()) # 입력 받은 값 두개 쪼갬
    graph[a] += [b] # a 에 b 연결
    graph[b] += [a] # b 에 a 연결 -> 양방향

# print(graph)

# visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시

# 처음에 visited[1]=1을 안 해도 1번 컴퓨터에 연결된 컴퓨터가 있다면, 연결은 쌍방향이니, 해당 컴퓨터 방문하고 다시 1번 컴퓨터 방문 

Q=deque([1]) 

while Q:
    c=Q.popleft()
    # nx : next
    for nx in graph[c]:
        if visited[nx] == 0:    # 방문 안했다면 방문 표시
            Q.append(nx)        # 다음 방문 컴퓨터 추가
            visited[nx] = 1

# 1번 컴퓨터는 이미 위에서 방문표시 해줬는데 여기서도 값이 추가 되기 때문에 -1 로 제외해준다. 
print(sum(visited)-1) 




