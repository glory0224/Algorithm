# 백준 1759번 암호 만들기 

# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.

#from itertools import combinations
# import sys

# L , C = map(int, sys.stdin.readline().split())

# A = sorted(list(map(str, input().split())))

# combi = list(combinations(A, 4))

# for i in combi:
#     for j in i:
#         print(j, end='')
#     print()
    
# cstw -> 하나가 더 나와서 출력 초과로 실패 

# ----------------------------------------------

# 백트레킹으로 풀이 
import sys

def back_tracking(cnt, idx):
    
    # 암호를 만들었을 때 
    if cnt == L:
        # 모음, 자음 체크 , 문제에서 최소 한개 모음과 두개의 자음으로 구성해야 한다고 했기 때문에
        vo, co = 0, 0
        
        for i in range(L):
            # 자음 배열에 이미 존재하면 모음 개수 증가
            if answer[i] in consonant:
                vo += 1
            else:
                co += 1
        
        # 모음 1개 이상이고 자음 2개 이상일 때 
        if vo >= 1 and co >= 2:
            print("".join(answer)) # 배열 -> 문자열 출력 

        return # 재귀 함수 종료 
    
    # 반복문을 통해서 암호를 생성
    for i in range(idx, C):
        answer.append(A[i])
        back_tracking(cnt +1, i + 1)
        answer.pop()

L , C = map(int, sys.stdin.readline().split())

A = sorted(list(map(str, input().split())))
# 자음 배열 생성 
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0,0)

