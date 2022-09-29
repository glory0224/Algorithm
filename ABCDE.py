# 백준 13023번 친구관계 ABCDE 문제 
# https://data-flower.tistory.com/104

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

relations = [[] for _ in range(n)]

# 방문 표시 (인원수 범위가 2000까지이기 때문에 2001로 설정)
visited = [False] * 2001

# 정답 변수 생성
ans = False

# 친구 관계 입력 받기(2차원 배열로 입력받는 방법..!)
for i in range(m):
    a , b = map(int, input().split())
    # 친구 관계 등록
    relations[a].append(b)
    relations[b].append(a)
    
#print(relations)

# dfs 재귀 함수

def dfs(idx, depth):
    global ans
    # 방문 표시
    visited[idx] = True

    # 종료 조건 : 친구 관계가 4번 이상 연결 되어 있을 시 종료 
    if depth == 4:
        # 정답 표시 후 리턴
        ans = True
        return
    
    # 친구 관계가 존재하는지 확인
    for i in relations[idx]:
        # 아직 방문하지 않았다면
        if not visited[i]:
            # 방문 표시
            visited[i] = True
            # 재귀적으로 함수를 실행
            dfs(i, depth + 1)
            visited[i] = False
            

# 0번부터 N-1번까지 확인하며    
for i in range(n):
    # 친구 관계 탐색
    dfs(i, 0)
    # 현재 방문 표시 해제 
    visited[i] = False
    
    # 친구 관계가 존재 했다면
    if ans:
        # 탈출한다
        break
    
# 정답이 있었다면 1 출력
if ans:
    print(1)

# 정답이 없었다면 0 출력
else:
    print(0)