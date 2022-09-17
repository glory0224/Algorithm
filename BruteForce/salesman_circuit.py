#10971번 외판원 순회 2 

#https://suri78.tistory.com/152


import sys

def move(now, depth):
    global cost, ans
    
    # 재귀 함수 종료 조건 
    if depth == N:
        if path[now][0] > 0:
            ans = min(ans, cost + path[now][0])
            # print("ans : " + str(ans))
        return

    # 방문을 했기 때문에 1로 변경해서 True 값 만들어준다.
    visited[now] = 1
    # {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
    for l in link[now]:
        if not visited[l]:
            # print("cost 전의 순수 값 " + str(path[now][l]))
            cost += path[now][l]
            # print(cost)
            move(l, depth + 1)
            cost -= path[now][l]
            # print("함수 종료 후 코스트 값 : "+str(cost))
    visited[now] = 0
            
N = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# 방문 확인 변수 
visited = [0]*N

# 방문할 수 없는 0을 제외시키기 위한 딕셔너리 
link = {}

cost, ans = 0, 10**7

# 방문할 도시 수만큼 2중 for문 돌면서 방문 하지 말아야할 도시 인덱스 구하기 
for i in range(N):
    link[i] = []
    for j in range(N):
       if path[i][j] > 0:
          link[i].append(j)
          
#print(link) # {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
 
move(0,1) 

print(ans)


