# 백준 2110번 공유기 설치

# 이분 탐색

# https://hongcoding.tistory.com/3

# 아이디어
# 1. distance라는 리스트에 집들의 좌표를 입력 받은 후 정렬한다.
# 2. start=1, end=distance[-1] - distance[0] 으로 설정. (시작값은 최소 거리, 끝 값은 최대 거리)
# 3. 앞 집부터 공유기 설치 
# 4. 설치할 수 있는 공유기 개수가 router개를 넘기면 더 넓게 설치 할 수 있다는 의미이기 때문에 설치 거리를 mid + 1로 설정 후 다시 앞집부터 설치
# 5. router개가 넘지 않는다면 더 좁게 설치 해야 한다는 의미로 mid - 1로 설정 

import sys

input = sys.stdin.readline

home, router = map(int, input().split())

distance = []

for i in range(home):
    distance.append(int(input()))

distance.sort()

def binary_search(distance, start, end):
    while start <= end:
        mid = (start + end) // 2
        # print("mid : " + str(mid))
        current = distance[0]
        count = 1

        for i in range(1, len(distance)):
            if distance[i] >= current + mid:
                # print("current + mid : " + str(current + mid))
                # print("distance[ "+str(i) +" ] : " + str(distance[i]))
                count += 1
                # print("count : " + str(count))
                current = distance[i]
        
        if count >= router:
            global answer
            start = mid + 1
            # print("공유기 개수보다 크거나 같을 때 start : " + str(start))
            # print("공유기 개수보다 크거나 같을 때 end : " + str(end))
            answer = mid
            
        else:
            end = mid - 1
            # print("end : " + str(end))



start, end = 1, distance[-1] - distance[0] # 정렬을 했기 때문에 배열에서 최대거리는 맨 뒤 배열 - 맨 앞 배열
answer = 0

binary_search(distance, start, end)

print(answer)


