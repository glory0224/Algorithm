# 백준 1991번 트리 순회

import sys

N = int(sys.stdin.readline())

# 딕셔너리 생성
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]
    #print(tree)


# 문제에서 설명한 순서대로 함수를 생성한다. 

def preorder(root): # 전위 순회
    if root != '.':
        print(root, end='') # root
        preorder(tree[root][0]) # left 위치
        preorder(tree[root][1]) # right
        
def inorder(root): # 중위 순회
    if root != '.':
        inorder(tree[root][0]) # left
        print(root, end='') # root
        inorder(tree[root][1]) # right

def postorder(root): # 후위 순회 
    if root != '.':
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root, end='') # root
        
# 최상위 루트인 A를 넣은 함수를 각각 실행해준다.
preorder('A')
print() # 개행
inorder('A')
print()
postorder('A')
