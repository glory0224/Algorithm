# 백준 1933번 스카이라인 문제 
# https://peisea0830.tistory.com/97 <- 설명이 잘 나와있으니 나중에 기억 안나면 참고 
# lamda 표현식이 이해 안될 때 참고할 사이트 https://stackoverflow.com/questions/62208185/what-does-arr-sortkey-lambda-x-x0-x1-mean

"""
    우선 순위 큐와 정렬, set을 적절히 사용한다.
    큐와 정렬, set의 특징을 잘 알고 있어야 문제 풀이가 쉬울 것 같다.
"""

import sys, heapq

# 입력

# 빌딩 개수 
n = int(sys.stdin.readline())

arr = []
height = [0] * n
q = []

# end : 현재 index번째 건물의 끝나는 지점을 저장하는 리스트 
end = [0] * n
# check : 현재까지 끝난 끝점을 저장하는 set
check = set()

for i in range(n):
    # 건물의 왼쪽 x 좌표, 높이, 오른쪽 x 좌표
    a, b, c = map(int, sys.stdin.readline().split())
    # 시작점이면 1, 끝점이면 -1
    arr.append((a, i, 1))
    # print("시작점 : " + str(arr))
    arr.append((c, i, -1))
    # print("끝점 : " + str(arr))
    height[i] = b
    # print("height[" + str(i) + "] : " + str(height[i]))
    end[i] = c


# 각각의 정렬 우선순위를 정할 수 있도록 lamda를 이용

# 첫번 째 우선순위 : 시점이 앞서는지
# 두번 째 우선순위 : 시점이 같다면 시작점인지
# 세번 째 우선순위 : 시점도 같고 둘 다 시작점이면 높이가 더 높은지

# print("sort 이전 arr : " + str(arr))
# arr.sort(key=lambda x : (x[0])) # 현재 예제 기준으로는 큰 변화가 없음, 그러나 경우의 수를 모두 생각해줘야 하기 때문에 탈락 
arr.sort(key=lambda x : (x[0], -x[2], -height[x[1]])) # 각각의 우선순위를 모두 고려

# print("sort 이후 arr : " + str(arr))

# now : 현재 최고 높이
now = 0
ans = []
for i in range(len(arr)):
    # point : 시점, idx :  건물의 인덱스, dir : 시작점인지 끝점인지
    point, idx, dir = arr[i]

    #print("point : " + str(point))
    #print("idx : " + str(idx))
    #print("dir : " + str(dir))

    # 시작점인 경우(빨간점)
    if dir == 1:
        # 높이가 갱신된다면 그 부분이 새로운 스카이라인
        # print("height[" + str(idx) + "] : " + str(height[idx]))
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
        # 높이가 갱신됨과 상관없이 현재 건물의 높이와 끝점을 최대 힙에 저장
        heapq.heappush(q, (-height[idx], end[idx]))
        # print(" 시작점 q : " + str(q))
        
    # 끝점인 경우(파란점)
    else:
        # 현재 시점이 끝났기 때문에 set에 끝점의 시점을 저장
        check.add(point)
        # print("check : " + str(check))
        # 최대 높이가 끝난 건물이 아닐 때까지 pop
        while q:
            # print("끝점 q : " + str(q))
            if q[0][1] not in check:
                break
            heapq.heappop(q)
        
        # 힙이 비었다면 스카이라인의 높이는 0으로 갱신
        if not q:
            if now:
                now = 0
                ans.append((point, now))

        # 힙이 있다면 현재 높이와 비교 시 변동이 있다면 그 높이가 그 다음으로 높은 건물이기 때문에
        # 스카이라인 높이 갱신
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))

for i in ans:
    print(i[0], i[1], end=' ')

