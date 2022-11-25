# 백준 1654번 랜선 자르기 

# 이진 탐색으로 풀 수 있는 대표적인 알고리즘 문제 

# https://claude-u.tistory.com/443

# 랜선의 길이를 움직여 랜선 개수를 채우는지 본다.

# 1) 가장 짤은 길이 1을 start로, 랜선 중 가장 긴 길이를 end로 둔다.
# 2) 이분 탐색이 끝날 때까지 while문을 돌린다. 
# 3) mid를 start와 end의 중간으로 두고, 모든 랜선 값을 mid로 나누어 총 몇개의 랜선이 나오는지 본다. 
# 4-1) 랜선이 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복
# 4-2) 랜선이 목표치 이하이면 mid-1을 end로 두고 다시 while문 반복
# 5) start와 end가 같다면? 조건을 만족하는 최대 랜선길이를 찾아 탈출
# 6) 결과 값인 end 출력



import sys 

input = sys.stdin.readline

myNum, needNum = map(int, input().split())

lan = [int(input()) for _ in range(myNum)] # 각각의 랜선 길이를 담는 배열 

start, end = 1, max(lan) # 이진탐색 처음과 끝위치, 끝 위치는 랜선에서 제일 긴 길이로

while start <= end: # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 # 중간 위치
    lines = 0 # 랜선 수
    for i in lan:
        lines += i // mid # 분할 된 랜선 수
        # print(str(i) + "//" + str(mid)) 
        # print("lines : " + str(lines))
    if lines >= needNum: # 랜선의 개수가 분기점
        start = mid + 1 # 만약 랜선의 개수를 필요개수 이상으로 만들 수 있다면 start 바꿔서 중간위치를 크게 만든다.
    else:
        end = mid - 1 # 만약 랜선의 개수가 필요개수 이상이 안된다면 중간 위치를 작게 바꾼다. 

print(end)


