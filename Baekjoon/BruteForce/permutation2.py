# 백준 10973번 이전 순열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
swap = 0
for i in range(n-1,0,-1):
    if arr[i-1] > arr[i]:
        swap = i-1 
        break
else:
    # 내림차순이 끝났을 때 -1 출력후 종료 
    print(-1)
    sys.exit()

for i in range(n-1,0,-1):
    if arr[swap] > arr[i]:
        arr[swap],arr[i] = arr[i],arr[swap]
        print(arr[swap])
        print(arr[i])
        print(arr[swap+1:]) # swap은 현재 3 + 1 = 맨 마지막 인덱스 값 2부터 뒤에 슬라이싱
        print(arr[:swap+1]) # swap = 4 인덱스 주소 4번 앞으로 슬라이싱        
        # 문제에서 가장 마지막의 오는 순열은 내림차순 해준다고 명시했기 때문에 sorted reverse 옵션 true로 정렬한다.
        arr = arr[:swap+1]+sorted(arr[swap+1:], reverse=True) # sorted(배열, reverse 옵션 ) : 내림차순으로 정렬하여 반환, 기본은 false로 오름차순이다.

        print(*arr)
        break
