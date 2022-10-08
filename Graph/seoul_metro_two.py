# 백준 16947번 서울 지하철 2호선 

# dfs와 bfs 둘다 이용하는 문제 

# https://data-flower.tistory.com/105 코드

import sys

from collections import deque

input = sys.stdin.readline
# dfs 사용시 제한을 임의로 늘려준다.
sys.setrecursionlimit(100000)

# 순환선이 존재하는지 확인하는 함수 
# start = 시작역, idx = 현재 역, cnt = 방문횟수, 두번 이상 다른 역 방문 시에만 순환역에 해당하도록 하기 위한 매개변수 
def circulation_station(start, idx, cnt):
    # 순환선인지 아닌지 여부 확인 전역 변수 
    global cycle

    # 방문한 역이 2곳 이상이고, 현재 역이 시작 역으로 돌아왔다면 
    if start == idx  and cnt >= 2:
        # 순환선이므로 True로 변경
        cycle = True
        return 
    # 현재 역에 대한 방문 표시 
    visited[idx] = True
    # 다음으로 방문할 역을 받으면서
    for i in info[idx]:
        # 아직 방문하지 않은 역일 경우 
        if not visited[i]:
            # 해당 역을 추가하고 재귀적으로 호출한다.
            circulation_station(start, i, cnt + 1)
        # 이미 방문을 한 역이면서 방문한 역이 2곳 이상이라면
        elif i == start and cnt >=2:
            # 방문하는 역을 그대로 재귀적 호출한다.
            circulation_station(start, i, cnt) 

# 역과 순환역 사이의 거리를 확인하는 함수 (bfs) 
def distance_station():
    global check
    q = deque()
    # 순환역에 속하는 역은 모두 거리가 0
    for i in range(T):
        if cycle_station[i]:
            check[i] = 0
            q.append(i)
    
    # 큐 안에 값이 없을 때까지 반복
    while q:
        # 현재 역
        now = q.popleft()
        # 다음 역 선택 
        for i in info[now]:
            # 역이 순환선에 포함되지 않는 역이라면 
            if check[i] == -1:
                # 큐에 추가
                q.append(i)
                # 이동 거리를 구한다.
                check[i] = check[now] + 1
    # 모든 각 역과 순환선 사이의 최소 거리를 출력한다.
    for i in check:
        print(i, end=' ')
        
    
# 역의 개수를 입력 받는다.
T = int(input())

# 역과 역을 연결하는 구간의 정보를 2차원 배열로 표현
info = [[] for _ in range(T)]

# 순환역을 표시하는 전체 역 - 해당역이 순환역인지 아닌지를 체크  
cycle_station = [False] * T
 
# 순환역이 아닌 역들과 순환선 사이의 거리 정답을 체크하기 위한 변수 선언
check = [-1] * T

# 역 구간의 정보 입력 받기
# ABCDE.py에서 관계 정보 입력 받을 때와 동일한 방식  
for _ in range(T):
    a, b = map(int, input().split())
    # dfs 시작 인덱스를 0부터 하기 때문에 list index out of range 오류를 막기 위해서 -1 처리 
    info[a-1].append(b-1)
    # info[a].append(b)
    info[b-1].append(a-1)
    # info[b].append(a)

# print(info)
    
# 순환선인지 확인
for i in range(T):
    # 방문 여부 표시 리스트
    visited = [False] * T
    # 순환선이 있는지 여부 확인 
    cycle = False
    # 순환선 탐색
    circulation_station(i, i, 0)
    # 순환선이 있다면 순환선에 속하는 역을 순환역으로 표시해준다.
    if cycle:
        cycle_station[i] = True

# 역 거리 확인 
distance_station()
    
