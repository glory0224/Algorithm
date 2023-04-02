# 백준 2343번 기타레슨 문제 
# 이분 탐색 
# https://jainn.tistory.com/232


import sys 

input = sys.stdin.readline

lecture, bluelay = map(int, input().split())

video = list(map(int, input().split()))

vm = max(video)
# 맨 끝이 제일 긴 비디오라고 생각하고 배열의 끝의 값으로 주면 반례로 제일 긴 비디오 값이 중간에 껴있는 상황이 발생한다. 
# 그렇기 때문에 배열의 최대값을 찾아 그것을 start로 만들고, end는 리스트의 총합을 넣는다. 
start, end = vm, sum(video) 


res = 10**9 # 큰 값을 넣고 min과 비교 

while(start <= end):
    # print("start : " + str(start))
    # print("end : " + str(end))
    mid = (start+end) // 2

    # print("mid : " + str(mid))
    cnt = 1
    tmp = 0
    for i in range(lecture):
        if(tmp+video[i] <= mid):
            # 만약 현재 블루레이에 비디오를 더 넣을 수 있다면
            tmp += video[i]
            # print("비디오를 넣는경우 tmp : " + str(tmp))
        else:
            cnt += 1
            tmp = video[i]
            # print("비디오를 넣지 못하는 경우 tmp : " + str(tmp))
        if(cnt > bluelay):
            break
    
    # print("cnt : " + str(cnt))
    if(cnt > bluelay):
        start = mid + 1
    else:
        end = mid - 1
        # print("else mid : " + str(mid))
        # print("else vm : " + str(vm))
        if(mid >= vm): # 블루레이의 최솟값을 찾기위해 값을 비교할 때, 리스트의 최대값보다 작다면 결과값에 넣지 않도록 조건을 넣어준다.
            res = min(res, mid) 


print(res)
