# 11723번 백준 집합


# for 문으로 접근 하려고 하면 시간초과가 난다. 

# import sys
# input = sys.stdin.readline()

# T = int(input)

# bit = []

# for i in range(T):
#     n = list(map(str, input.split()))
    
#     if n[0] == 'add':
#         bit.append(n[1])
#     elif n[0] == 'check':
#         if n[1] in bit[i]:
#             bit[i] = "1"
#         else:
#             bit[i] = "0"
#     elif n[0] == 'remove':
#         if n[1] in bit[i]:
#             bit.pop()
#         else:
#             continue
#     elif n[0] == 'toggle':
#         if n[1] in bit[i]:
#             bit.pop()
#         else:
#             bit.append(n[1])
#     elif n[0] == 'all':
#         bit.reverse()
    
#     elif n[0] == 'empty':
#         bit.clear()
        
# print(bit)


# SET을 이용해서 풀 수 있다.

import sys

t = int(sys.stdin.readline())
S = set()

for _ in range(t):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        # empty? 처리
        else:
            S = set()
    
    else:
        func, x = temp[0] , temp[1]
        x = int(x)
        
        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

# remove 함수 대신 discard 함수를 써서 제거하는 이유는 remove는 
# 존재하지 않는 수를 제거하려고 하면 오류를 발생하는데 
# discard함수를 사용하면 오류가 나지않고 정상종료할 수 있다.
