# 백준 13549번 숨바꼭질 3 문제 

# 숨바꼭질 문제에서는 '초' 에 해당하는 가중치가 1이었지만 지금은 0(순간이동), 1(일반이동) 두가지로 나눈다.

# 따라서 큐를 두가지로 나눠서 구현한다.

# 여기서 양방향 큐인 deque를 활용하면서 큐 2개를 별도로 만들지 않고, 순간이동 할 경우 맨 앞에 값 추가, 이동한 값은 뒤에 값을 추가한다.

# deque는 기본적으로 append할 때 순차적으로 정렬된다. 

from collections import deque


MAX = 10 ** 5
dist = [-1] * (MAX + 1)
check = [False] * (MAX + 1)

subin, sister = map(int, input().split())

q = deque()
q.append(subin) # 초기값
check[subin] = True # 시작 위치 방문 표시
dist[subin] = 0 # 시작 거리 초기화

while q:
    now = q.popleft()
    
   
    if now * 2 <= MAX and check[now*2] == False: # 순간이동
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now] # 0초 
    if now + 1 <= MAX and check[now + 1] == False: # x + 1 이동
        q.append(now + 1) 
        
        check[now +1] = True
        dist[now + 1] = dist[now] + 1 # 1초 증가 
    if now - 1 >= 0 and check[now - 1] == False: # x - 1 이동
        q.append(now - 1)
        
        check[now - 1] = True
        dist[now - 1] = dist[now] + 1 # 1초 증가
        
print(dist[sister]) # 해당 MAX 범위까지 다 돌고 sister 좌표에 해당하는 곳에 도달했을 때 가중치(최소 시간) 확인
