# 백준 2250번 파이썬

# https://velog.io/@imacoolgirlyo/2020-02-04-1702-%EC%9E%91%EC%84%B1%EB%90%A8-ksk67m6221

import sys


N = int(sys.stdin.readline())
parentNode = [-1]*(N+1) # 부모노드가 항상 1로 시작하지는 않기 때문에 부모노드를 저장할 배열을 따로 만든다.
tree = {}
root = 0 # root 노드 초기화

# 트리 생성
for _ in range(N):
    v, left, right = map(int, sys.stdin.readline().split())
    tree[v] = [left, right]
    if left != -1:
        parentNode[left] = v
    if right != -1:
        parentNode[right] = v
#print(tree)
#print(parentNode)        

# 루트 노드 찾기(루트노드가 될 수 있는 조건인 -1에 해당하는 노드 찾기)
for i in range(1, N+1):
    if parentNode[i] == -1:
        root = i
        #print(i)

level_min = [N]*(N+1) # 각 레벨의 최소, 최대 idx 저장
level_max = [0]*(N+1)
level = [0] * (N+1)
level[root] = 1 # 최상위 레벨 루트 값 1
cur = 0

# 중위 순회
def in_order(key): 
    global cur
    # print("key : " + str(key))
    if tree[key][0] != -1: # 왼쪽에 노드가 존재하면
        level[tree[key][0]] = level[key] + 1 # 왼쪽 노드의 레벨은 현재 레벨 + 1
        in_order(tree[key][0]) # 왼쪽 노드의 끝까지 이동하면 재귀적으로 종료한다.
        
    cur += 1 # 노드를 방문하면서 1부터 N까지 idx를 증가시킨다.
    
    if level_min[level[key]] > cur:
        level_min[level[key]] = cur # 현재 레벨의 가장 왼쪽 노드의 idx를 갱신한다.
        #print("최소값 : " + str(level_min[level[key]]))
    if level_max[level[key]] < cur:
        level_max[level[key]] = cur
        #print("최대값 : " + str(level_max[level[key]]))
    if tree[key][1] != -1: # 오른쪽 노드 존재하면 
        level[tree[key][1]] = level[key] + 1 # 오른쪽 노드의 현재 레벨 + 1
        in_order(tree[key][1]) # 오른쪽 노드 끝까지 이동하면 재귀적으로 종료한다.
    
    return

in_order(root)

#결과 인덱스, 결과 값 변수 초기화
result = 0 
result_idx = 0

# 차이를 찾는다.
for i in range(1, N+1):
    # print("level_max : " + str(level_max[i]))
    # print("level_min : " + str(level_min[i]))
    diff = level_max[i] - level_min[i] + 1
    if result < diff:
        result = diff
        result_idx = i
        # print("result : " + str(result))
        # print("result_idx : " + str(result_idx))

print(result_idx, result)





