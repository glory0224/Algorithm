# 백준 14889번 스타트와 링크 문제 

# 재귀 함수 조건 참고 https://hyojin96.tistory.com/entry/%EC%9E%AC%EA%B7%80%ED%95%A8%EC%88%98 , https://gothone7092.tistory.com/35

# 풀이 https://ji-gwang.tistory.com/260

# 재귀함수로 문제 해결

import sys

input = sys.stdin.readline

T = int(input())

array = []
result = 1e9 # 결과 값을 출력해주기 위해서 문제의 범위를 벗어나게 큰 수로 초기화 한다. 
visited = [False] * (T + 1) # 방문 여부 확인용 visited

# array에 입력값 담아준다.
for i in range(T):
    array.append(list(map(int, input().split())))
    

def solve(depth, idx):
    global result
    
    # 재귀 함수 기반조건에 해당한다. 
    if depth == (T // 2): # 몫 == depth
        start, link = 0 ,0 # start팀, link팀 각각 초기화 
        for i in range(T):
            for j in range(i + 1, T): # 이차원 배열 돌면서 처음
                print("array" + str(i) + "번째" + str(j) + "번째" + "값 : " + str(array[i][j]))
                print("i 값 : " + str(visited[i]))
                print("--------------------------------")
                print("j 값 : " + str(visited[j]))
                if visited[i] and visited[j]:
                    start += (array[i][j] + array[j][i])
                    print("start에 저장" + str(start))
                elif not visited[i] and not visited[j]:
                    print(str(array[i][j]))
                    print(str(array[j][i]))
                    link += (array[i][j] + array[j][i])
                    print("link에 저장" + str(link))
        
        
        result = min(result, abs(start - link))
    for i in range(idx, T):
        print("현재 depth : " + str(depth))
        print("현재 i 인덱스 : " + str(i))
        if not visited[i]:
            visited[i] = True
            solve(depth + 1, i + 1)
            visited[i] = False
            
solve(0,0)
print(result)


