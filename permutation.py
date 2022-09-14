# 백준 10972번 순열 문제
# 뒤에서부터 현재 인덱스와 이전 인덱스를 비교하면서 swap해주는 방식으로 문제를 푼다.  

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
swap = 0
for i in range(n-1,0,-1):
    if arr[i-1] < arr[i]:
        swap = i-1 
        break
else:
    # 내림차순이 끝났을 때 -1 출력후 종료 
    print(-1)
    sys.exit()

for i in range(n-1,0,-1):
    if arr[swap] < arr[i]:
        arr[swap],arr[i] = arr[i],arr[swap]        
        arr = arr[:swap+1]+sorted(arr[swap+1:])

        print(*arr)
        break