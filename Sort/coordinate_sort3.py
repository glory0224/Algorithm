# 백준 10989번 수 정렬하기 3

# 일반적인 문제라고 생각하고 풀면 메모리 문제로 바로 틀림
# 공간 복잡도를 줄여야 하는 문제 
# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
# 일반적으로 입력값이 크지않은 경우에는 상관없지만 이렇게 입력값이 극한으로 많이 주어질 때에는
# 메모리를 좀 더 효율적으로 관리해야한다.

# 참고로 파이썬은 내부적으로 연산과 메모리를 관리하기 때문에 파이썬에 내장되어있는 함수들을 적용할수록
# 메모리를 효율적으로 관리할 수 있다고 한다.

# import sys

# input = sys.stdin.readline

# N = int(input())

# num = []

# for i in range(N):
#     num.append(list(map(int, input().split())))


# num.sort(key=lambda x: x[0])

# for i in num:
#     print(i)


import sys

input = sys.stdin.readline

N = int(input())

# 입력 값으로 10000개까지 주어졌기 때문에 10000개만큼의 리스트 생성 
# num = [] # 공백으로 선언하면 메모리를 많이 쓴다. 
num = [0] * 10001

# 리스트에 각 요소마다 0을 할당해놓고 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해준다.
for i in range(N):
    num[int(input())] += 1

# 나중에 입력을 다 받고나면  0이 아닌 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력
for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
