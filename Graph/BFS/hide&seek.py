# 백준 1697번 숨바꼭질 문제 

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하기

# https://wook-2124.tistory.com/273 참고

import sys
from collections import deque

def bfs():
    q = deque()
    # 탐색 시작 위치 =  수빈 위치 
    q.append(subin)
    while q:
        x = q.popleft()
        # 동생의 위치까지 도달하면 종료 
        if x == sister:
            print(dist[x]) # 거리 반환
            break
        # bfs 탐색가능한 범위를 nx로 뽑아준다.
        for nx in (x - 1, x + 1, x *2):
            if 0<= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)    # q = deque([4, 6, "10"])    

MAX = 10 ** 5 # 시간초과 방지로 값을 직접 제한한다.
dist = [0] * (MAX + 1) # for문을 돌면서 방문 여부 확인을 위해 + 1 


subin, sister = map(int, input().split())

bfs()
