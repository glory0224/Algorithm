#16964번 DFS 스페셜 저지
# https://vixxcode.tistory.com/29

# 자신을 포함한 총 길이를 저장하여 시간초과를 피한 코드 


import sys 
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
children = [set() for _ in range(N+1)]

# 연결된 간선 그래프 생성
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 비교할 테스트 배열 입력받기 
test_case = list(map(int, input().split()))
level = [False] * (N+1)
# 각 레벨 트리의 사이즈를 담기위한 배열 
tsize = [0] * (N+1)
# 방문 여부 확인 
visited = [False] * (N+1)

#DFS 함수 - 시작값, 레벨을 매개변수로 받는다.
def dfs(x, lv):
    # 방문 했다면 바로 반환
    if visited[x]:
        return 0
    # 방문 표시 
    visited[x] = True
    
    # 해당 노드의 크기를 담기 위한 사이즈 변수 
    size = 1
    level[x] = lv
    for i in range(len(graph[x])):
        next = graph[x][i]
        # 각 하위 레벨의 노드를 dfs로 탐색하면서 size를 파악
        size += dfs(next, lv + 1)
    tsize[x] = size
    # print("size : " ,size)
    # print(str(x) + "번째 노드 및 하위 노드 tsize 값 :" + str(tsize[x]))
    # print("lv : ", lv)
    return size

if test_case[0] != 1:
    print("0")
    sys.exit(0)
else:
    dfs(1, 0)
    for i in range(1, N):
        x = test_case[i]
        # 자식노드가 없고 자기 자신만 있거나 주어진 범위를 벗어난 경우를 continue 처리 
        if tsize[x] == 1 or i + tsize[x] >= N:
            continue
        
        next = test_case[i + tsize[x]] # 1 + 2 = 3
        # print(str(i) + "번째 else의 next 값 : " , next)
        if level[next] > level[x]:
            print(0)
            sys.exit(0)
    print(1)

            