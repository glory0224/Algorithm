# 백준 1981번 배열에서 이동
# BFS + BinarySearch
# https://chldkato.tistory.com/67


# 아이디어 

# 1. 목적지까지 도착할 수 있는 범위의 왼쪽, 오른쪽에 대한 범위를 구한다.
# 2. bfs로 목적지에 도착하면 최소값을 갱신하고 범위의 왼쪽 값을 증가시킨다.
# 3. 도착할 수 없으면 범위의 오른쪽값을 증가시킨다. 만약 왼쪽과 오른쪽을 이전에 증가한 경우가 있으면 왼쪽과 오른쪽을 둘다 증가시켜 다음 범위를 체크한다. 
# 4. 모든 경우를 확인한 후 최소값을 출력 

import sys
from collections import deque

input = sys.stdin.readline

# 좌표 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# dfs 함수
def bfs():
    q = deque()
    c = [[0]*T for _ in range(T)]
    q.append([0, 0])
    c[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == T-1 and y == T-1:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < T and 0 <= ny < T:
                if left <= nums[nx][ny] <= right and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])

T = int(input())

nums, r_max, l_min = [], 0, sys.maxsize

for _ in range(T):
    row = list(map(int, input().split()))
    nums.append(row)
    l_min = min(l_min, min(row))
    r_max = max(r_max, max(row))

l_max = min(nums[0][0], nums[T-1][T-1])
r_min = max(nums[0][0], nums[T-1][T-1])

left, right = l_min, r_min

ans = sys.maxsize

while l_min <= left <= l_max and  r_min <= right <= r_max:
    l_flag, r_flag = 0, 0
    if bfs():
        ans = min(ans, right - left)
        left += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            left += 1
            right += 1
        else:
            right += 1
            r_flag = 1

print(ans)

