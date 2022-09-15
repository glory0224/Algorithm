# 10974번 백준 모든 순열

# dfs로 풀 수 있다.

def dfs(depth):
    

    # 탐색을 모두 마쳤을 때 재귀함수 종료를 위한 depth == n 비교 
    if depth == n:
        print(*visited)
    else:
        for i in range(n):
            if i + 1 in visited:  # visited 배열로 비교해서 검사한다. 
                continue
            visited[depth] = i + 1 # 맨 앞은 결국 1, 2, 3 순서대로 n 범위까지 for문 돌면서 재귀 함수 호출
            dfs(depth + 1)
            visited[depth] = 0 


n = int(input())
visited = [0] * n
dfs(0)


    