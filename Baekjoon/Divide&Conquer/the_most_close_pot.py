# 백준 2261번 가장 가까운 두 점 
# https://casterian.net/algo-prob/boj2261.html - 이론 설명
# https://my-coding-notes.tistory.com/103 - 문제 풀이 


# closest pair problem 

# 가지 치기

"""
    Closest Pair algorithm

    1. 모든 점을 x 좌표를 기준으로 정렬
    2. 점들의 중앙값을 기준으로 양분할
    3. 2개 까지로 분할되면 점 사이의 최소 거리를 찾고, 해당 거리보다 x좌표끼리 가까운 것만 후보 점으로 등록
    4. y좌표 기준으로도 정렬하고 y좌표 차이가 최소 거리보다 낮은 것들만 대상으로 거리를 계산
"""

import sys
input = sys.stdin.readline

n = int(input())
pl = [list(map(int, input().split())) for i in range(n)]

# x축 기준 정렬
pl.sort()
# print("pl : " + str(pl))


# 두 점 사이의 거리 계산 함수 
def getDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def dac(start, end):
    # 점 하나의 거리는 없으니 최대값 리턴 
    # print("start : " + str(start))
    # print("end : " + str(end))

    if start == end:
        return float('inf')

    # 점이 두 개 남으면 사이의 거리 리턴
    if end - start == 1:
        return getDist(pl[start], pl[end])

    # 분할 정복 실행
    mid = (start + end) // 2
    # print("mid : " + str(mid))
    minDist = min(dac(start, mid), dac(mid, end))
    # print("minDist : " + str(minDist))

    # x축 기준으로 후보 점들을 찾는다.
    target_pl = []

    #분할 정복 후 start, end
    # print("분할 정복 후 start : " + str(start))
    # print("분할 정복 후 end : " + str(end))
    for i in range(start, end + 1):
        if (pl[mid][0] - pl[i][0])**2 < minDist:
            target_pl.append(pl[i])
            # print("target_pl : " + str(target_pl))

    # y축 기준 정렬
    target_pl.sort(key=lambda x: x[1])
    # print("y축 기준 정렬 : " + str(target_pl))
    # y축 기준으로 후보 점들 사이의 거리 비교
    t = len(target_pl)

    for i in range(t-1):
        for j in range(i+1, t):
            if (target_pl[i][1] - target_pl[j][1])**2 < minDist:
                minDist = min(minDist, getDist(target_pl[i], target_pl[j]))
            else:
                break
                # 현재 후보 점이 다음 점과 최소 거리보다 멀다면 더 볼 필요가 없다. 
                # 위의 처리를 하지 않는다면 시간 초과가 발생한다. 
    
    return minDist

print(dac(0, n-1))
