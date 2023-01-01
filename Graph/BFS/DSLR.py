# https://paris-in-the-rain.tistory.com/94
# https://pacific-ocean.tistory.com/388
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    q = deque()
    q.append([a, ""])
    while q:
        number, result = q.popleft()
        dn = (number * 2) % 10000
        if dn == b: return result + "D"
        elif arr[dn] == 0:
            arr[dn] = 1
            q.append([dn, result + "D"])
        sn = number - 1 if number != 0 else 9999
        if sn == b: return result + "S"
        elif arr[sn] == 0:
            arr[sn] = 1
            q.append([sn, result + "S"])
        ln = int(number % 1000 * 10 + number / 1000)
        if ln == b: return result + "L"
        elif arr[ln] == 0:
            arr[ln] = 1
            q.append([ln, result + "L"])
        rn = int(number % 10 * 1000 + number // 10)
        if rn == b: return result + "R"
        elif arr[rn] == 0:
            arr[rn] = 1
            q.append([rn, result + "R"])
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    arr = [0 for i in range(10000)] # 방문 여부를 True False가 아닌 0과 1로 구분한다. True와 False로 리스트를 만들어서 조회하면 시간초과가 발생했다. 

    print(bfs())
