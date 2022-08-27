# 백준 1149번 RGB거리 

T = int(input())

# A[i][0], A[i][1], A[i][2] 집의 색깔이 빨강, 초록, 파랑을 0, 1, 2로 담기 위한 2차원 배열 초기화
A = []

# 입력 값 T까지 돌면서 입력 리스트를 담아준다.
for i in range(T):
    A.append(list(map(int, input().split())))

# print(A) #[[26, 40, 83], [49, 60, 57], [13, 89, 99]]

for i in range(1, len(A)):
    # 빨강색 집이 마지막에 올 때 올 수 있는 최소값의 범위 : min(초록, 파랑) + 빨강
    A[i][0] = min(A[i-1][1], A[i -1][2]) + A[i][0]
    # 초록색 집이 마지막에 올 때 올 수 있는 최소값의 범위 : min(빨강, 파랑) + 초록 
    A[i][1] = min(A[i-1][0], A[i -1][2]) + A[i][1]
    # 파랑색 집이 마지막에 올 때 올 수 있는 최소값의 범위 : min(빨강, 초록) + 파랑
    A[i][2] = min(A[i-1][0], A[i -1][1]) + A[i][2]

# index 배열을 0부터 시작했기 때문에 T - 1 으로 결과값 조회 
# bottom up 방식으로 최소값을 비교하면서 마지막 배열 A[i-1]번째의 빨강, 초록, 파랑 비용의 최소값들을 구하고 그 중에 min 함수를 사용하여 최소값을 구한다. 
print(min(A[T-1][0], A[T-1][1], A[T-1][2]))

