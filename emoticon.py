# 백준 14226번 이모티콘

# https://data-flower.tistory.com/80

from collections import deque

S = int(input())
q = deque()
# (현재 이모티콘 개수, 클립보드에 있는 개수)
q.append((1,0))
# 2차원 리스트를 만들 수 있으나 불필요한 정보가 많기 때문에 방문 표시를 딕셔너리로 표현한다.
visited = dict()
visited[(1,0)] = 0

# 너비 우선 탐색 실행
while q:
    # 보통 bfs는 방문 가능한 전체 간선을 하나의 변수로 받지만
    # 지금 문제에서는 현재 개수와 클립보드 개수를 각각 뽑아준다.
    now , clip = q.popleft()
    # 현재 이모티콘 개수가 s개라면
    if now == S:
        # 걸린 시간 출력
        print(visited[(now, clip)]) 
        break
    
    # print(visited.keys())
    
    # 1. 화면에 있는 이모티콘을 모두 복사하기 
    if(now, now) not in visited.keys():
        visited[(now, now)] = visited[(now, clip)] + 1 # 방문 표시
        q.append((now, now))
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if(now + clip, clip) not in visited.keys():
        visited[(now + clip, clip)] = visited[(now, clip)] + 1 # 방문 표시
        q.append((now + clip, clip))
    # 3. 화면에 있는 이모티콘 중 하나를 삭제하기
    if(now - 1, clip) not in visited.keys():
        visited[(now - 1, clip)] = visited[(now,clip)] + 1 # 방문 표시
        q.append((now-1, clip))
        