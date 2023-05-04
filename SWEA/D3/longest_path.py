# 최장 경로 (bfs 방식)

# N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산하자.

# 정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.

# 경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.

# 경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 두 개의 자연수 N M(1 ≤ N ≤ 10, 0 ≤ M ≤ 20)이 주어진다.

# 두 번째 줄부터 M개의 줄에 걸쳐서 그래프의 간선 정보를 나타내는 두 정수 x y(1 ≤ x, y ≤ N)이 주어진다.

# x와 y는 서로 다른 정수이며, 두 정점 사이에 여러 간선이 존재할 수 있다.


# [출력]

# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 그래프에서의 최장 경로의 길이를 출력한다.

# 입력
# 2
# 1 0  # 정점 개수 : 1개 간선의 개수 : 0개 - 간선의 개수가 없기 때문에 x, y가 따로 없음 
# 3 2  # 정점 개수 : 3개 간선의 개수 : 2개 - 간선의 개수가 존재하기 때문에 아래 2개의 간선 정보가 x y 로 입력받음
# 1 2
# 3 2

# 출력
# #1 1
# #2 3

def dfs(graph, v, visited, start): # 그래프 간선 정보, 정점개수, 방문여부, 시작정점을 매개로 하는 dfs 함수
    # 방문처리
    visited[start] = True
    # 최대 길이 초기화 - dfs 함수를 계속 호출하기 때문에 초기화 필요
    max_length = 0
    for i in graph[start]:
        if not visited[i]:
            length = dfs(graph, v, visited, i)
            if max_length < length:
                max_length = length
    
    visited[start] = False # DFS 함수가 끝나면서 방문 여부도 초기화 
    return max_length + 1 # 현재 노드와 자식 노드 사이의 간선을 하나 추가하기 때문에 + 1 , 최장 길이는 간선의 개수

def find_longest(graph, v):
    longest_path = 0
    for i in range(1, v+1):
        visited = [False] * (v+1)
        length = dfs(graph, v, visited, i)
        if longest_path < length: # 최장 길이 갱신
            longest_path = length
    return longest_path 

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split()) 
    if e == 0:
        longest_path = 1
    else:    
        # 인접 리스트로 그래프 정보를 입력받는다.
        graph = [[] for _ in range(v+1)]

    # 간선 정보 확인
        for j in range(e):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        longest_path = find_longest(graph, v)
    
    print(f"#{tc} {longest_path}")

        

