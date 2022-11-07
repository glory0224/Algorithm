# 백준 11728번 배열 합치기 
# 병합 정렬 
#https://jokerldg.github.io/algorithm/2021/08/03/array-combine.html


"""
아이디어 
1. 병합정렬 이용
 - 각 배열에 입력을 받는다.
 - A배열과 B배열을 합친다.
 - 합친 배열을 정렬하고 파이썬의 * 을 이용하여 출력한다.

2. 투 포인터 이용
 - 각 배열에 입력을 받는다. 
 - a와 b의 포인터를 생성하여 두 포인터가 각 배열의 끝이 아닐때 까지 진행한다.
 - a포인터의 길이가 A배열의 끝에 다왔다면 B배열의 값을 추가한다.
 - b포인터의 길이가 B배열의 끝에 다왔다면 A배열의 값을 추가한다. 
 - 두 배열의 길이가 끝이 아닌 경우 각 배열의 포인터의 크기를 비교하여 더 작은 값을 넣어준다. 

"""

# 1번 아이디어 풀이 
# import sys

# read = lambda: sys.stdin.readline().rstrip()

# N, M = map(int, read().split())

# A = list(map(int, read().split()))
# B = list(map(int, read().split()))

# answer = A + B
# answer.sort()

# print(*answer)

# 2번 아이디어 풀이 

import sys

read = lambda: sys.stdin.readline().rstrip()

N, M = map(int, read().split())

A = list(map(int, read().split()))
B = list(map(int, read().split()))
answer = []

a_pointer, b_pointer = 0, 0
a_length, b_length = len(A), len(B)

while a_pointer != a_length or b_pointer != b_length:
    if a_pointer == a_length:
        answer.append(B[b_pointer])
        b_pointer += 1
    elif b_pointer == b_length:
        answer.append(A[a_pointer])
        a_pointer += 1
    else:
        if A[a_pointer] < B[b_pointer]:
            answer.append(A[a_pointer])
            a_pointer += 1
        else:
            answer.append(B[b_pointer])
            b_pointer += 1
            
print(*answer)