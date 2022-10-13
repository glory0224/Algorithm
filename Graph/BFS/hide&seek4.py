# 백준 13913번 숨바꼭질 4

# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.

from collections import deque

# 해당 경로를 출력해주는 메소드
def path(x):
    # 경로를 넣어줄 배열 생성
    arr = []
    # 해당 위치를 temp에 담는다.
    temp = x
    for _ in range(dist[x] + 1): # 최소 시간까지 for문을 돌면서 
        arr.append(temp) # 해당 위치를 넣는다.
        temp = move[temp] # temp 변수 초기화 
    #print(' '.join(map(str, arr[::-1]))) # 배열의 역순으로 출력
    print(*arr[::-1]) # 파이썬 문법을 이용해서 출력도 가능하다.
    # print(' '.join(arr[::-1])) -> error

# bfs 메소드
def bfs():
    q = deque()
    q.append(subin)
    while q:
        x = q.popleft()
        if x == sister:
            # 거리 반환
            print(dist[x])
            # 이동 루트를 찍어주는 함수 호출
            path(x)            
            break
        
        for nx  in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                move[nx] = x
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10 ** 5
subin, sister = map(int, input().split())
dist = [0] * (MAX + 1)
move = [0] * (MAX + 1)

bfs()
