#6603번 로또

# https://pacific-ocean.tistory.com/238 코드


# 조합 라이브러리를 이용해서 풀기 
from itertools import combinations

while True:
    s = list(map(int, input().split()))
    # 종료 조건
    if s[0] == 0:
        break
    del s[0]  # 문제 출력을 보면 앞에 수가 하나씩 빠져서 출력 되기 때문에 인덱스 0 값 제거 
    s = list(combinations(s, 6))
    #print(s)
    for i in s:        
        for j in i:
            # print(j)
            print(j, end=' ')
        print() # print end 옵션으로 옆으로 쭉 나열되기 때문에 print()로 줄바꿈 처리 해준다. 
    print() # 출력 답에 개행이 되어 있기 때문에 print를 한번 더 해줘서 서로 간격을 띄어준다. 


# dfs로 문제 풀기 

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')        
        print()
        return    
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
        
combi = [0 for i in range(13)] # 6개의 인덱스로 조합을 짤 때 최대 수가 0 ~ 13 사이의 수이기 때문에 이렇게 지정
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()


