# 백준 2606번 바이러스 문제 (dfs 풀이)

# https://bio-info.tistory.com/152

n=int(input()) # 컴퓨터 연결 개수 입력
v=int(input()) # 연결선 개수

graph = [[] for i in range(n+1)] # 그래프 초기화

visited=[0]*(n+1) # 방문한 컴퓨터인지 표시

for i in range(v): # 그래프 생성
    a,b = map(int, input().split()) # 입력 받은 값 두개 쪼갬
    graph[a] += [b] # a 에 b 연결
    graph[b] += [a] # b 에 a 연결 -> 양방향

def dfs(v):
    visited[v] = 1 # 방문 표시
    for nx in graph[v]: 
        if visited[nx] == 0: # 방문 안했다면
            dfs(nx) # graph 에 있는 컴퓨터 번호를 재귀적으로 방문

dfs(1) # 방문할 컴퓨터 번호가 1
print(sum(visited)-1)

#  여기서 dfs함수에 visited를 인자로 입력받지도 않고, return하지도 않았는데 어떻게 print(sum(visited)-1)이 정답이 되는지?
# visited는 리스트로 파이썬의 리스트는 함수 밖에서 선언되어, 함수 내부에서 변경되어도, 함수 밖에서 변경이 적용이 가능하다.
# 즉, dfs함수 내부에서 변경된 visited 리스트는 함수 밖에서도 변경이 적용되기 때문에, sum(visited) - 1이 정답이 된다.
