# 백준 12886번 돌 그룹 문제 

# https://data-flower.tistory.com/83

from collections import deque

# 너비 우선 탐색 함수
def bfs():
    global A, B, C, total, visited
    q = deque()
    # 두 그룹 큐에 넣기
    q.append((A, B))
    # 방문 표시
    visited[A][B] = True
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 총 돌의 개수는 항상 일정하므로 남은 그룹 돌 개수 계산 가능
        z = total - x - y
        if x == y == z:
            print(1)
            return
        # 두 그룹끼리 돌의 개수 비교(같게 만들어주기 위한 코드)
        for A, B in (x, y), (y, z), (x, z):
            if A < B:
                B -= A
                A += A
            elif A > B:
                A -= B
                B += B
            # 돌의 개수가 같은 그룹은 건너뛴다.
            else:
                continue
            # 두 그룹이 돌을 분배한 후 남은 그룹의 돌 개수
            C = total - A - B
            # 가장 작은 값을 x, 가장 큰 값을 y로 받아준다.
            x = min(A, B, C)
            y = max(A, B, C)
            # 중복 제거
            # 해당 돌의 개수만큼 아직 분배되지 않았다면
            if not visited[x][y]:
                # 분배 실시
                q.append((x, y))
                # 방문 표시
                visited[x][y] = True
    print(0)            




# 돌 정보 입력 받기
A, B, C = map(int, input().split())
# 전체 돌의 개수
total = A + B + C
# 방문 표시
visited = [[False] * (total + 1) for _ in range(total + 1)]

# 총 돌의 개수가 3의 배수가 아니라면
if total % 3 != 0:
    # 같은 개수로 만들 수 없으므로 0 출력
    print(0)
# 3의 배수라면
else:
    #bfs 함수 실행
    bfs()