# 백준 1080번 행렬 문제 

# https://velog.io/@dding_ji/baekjoon-1080
# https://puleugo.tistory.com/39
# 위의 글 참고 


from sys import stdin

N, M = map(int, stdin.readline().split())

A = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
cnt = 0 

# 3*3 크기의 부분 행렬을 뒤집어주는 기능 구현 함수 
def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]
 
 
           
for i in range(N - 2): # 줄바꿈 가능 횟수 
    for j in range(M - 2): # 가로 줄 이동 가능 횟수 
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1
            
        if A == B:
            break 
        
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(cnt)