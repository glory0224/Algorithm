# 백준 1891번 사분면 문제 

"""
아이디어 

1. 주어지는 사분면에서 범위를 축소하면서 조각 번호의 위치를 찾는다. 각 i와 j의 초기 범위는 0 <= i < 2**d, 0 <= j 2**d

2. 찾은 위치에 각각 y와 x를 더해주면 찾고자 하는 값의 위치가 나오는데 이 좌표를 함수를 통해서 좌표가 속한 범위를 축소해간다. 한번 축소할 때마다 해당 사분면의 값을 answer에 더해준다. 

3. answer의 길이가 d와 같을 때 answer를 반환한다. 

"""

# 조각 번호의 위치를 찾는 함수 

def find(n1, n2, m1, m2, idx):
    if idx == len(number):
        return n1, m1
    
    if number[idx] == '1': # 1사분면 시작
        # print("----------1사분면 ---------")
        # print("(n1+n2)//2 : " + str((n1+n2)//2))
        # print("n2 : " + str(n2))
        # print("m1 : " + str(m1))
        # print("(m1+m2)//2 : " + str((m1+m2)//2)) 
        return find(n1, (n1+n2)//2, (m1 + m2)//2, m2, idx + 1)
    elif number[idx] == '2': # 2사분면 시작
        return find(n1, (n1 + n2)//2, m1, (m1+m2)//2, idx+1)
    elif number[idx] == '3': # 3사분면 시작
        # print("-------3사분면----------")
        # print("(n1+n2)//2 : " + str((n1+n2)//2))
        # print("n2 : " + str(n2))
        # print("m1 : " + str(m1))
        # print("(m1+m2)//2 : " + str((m1+m2)//2))
        return find((n1+n2)//2, n2, m1, (m1+m2)//2, idx+1)
    elif number[idx] == '4': # 4사분면 시작
        # print("----------4사분면 ---------")
        # print("(n1+n2)//2 : " + str((n1+n2)//2))
        # print("n2 : " + str(n2))
        # print("m1 : " + str(m1))
        # print("(m1+m2)//2 : " + str((m1+m2)//2)) 
        return find((n1+n2)//2, n2, (m1+m2)//2, m2, idx+1)

# 좌표가 속한 범위를 축소해가는 함수

def check(n1, n2, m1, m2):
    global answer
    if len(answer) == int(d):
        return answer

    if n1 <= nx < (n1 + n2)//2 and (m1 + m2) // 2 <= ny < m2:
        answer += '1'
        return check(n1, (n1 + n2) // 2, (m1 + m2) // 2, m2)
    elif n1 <= nx < (n1+n2)//2 and m1 <= ny < (m1+m2)//2:
        answer += '2'
        # print("---------- check 2사분면 ---------")
        # print("(n1+n2)//2 : " + str((n1+n2)//2))
        # print("n2 : " + str(n2))
        # print("m1 : " + str(m1))
        # print("(m1+m2)//2 : " + str((m1+m2)//2)) 
        return check(n1, (n1 + n2) // 2, m1, (m1 + m2) // 2)
    elif (n1+n2)//2 <= nx < n2 and m1 <= ny < (m1+m2)//2:
        answer += '3'
        return check((n1+n2) // 2, n2, m1, (m1 + m2) // 2)
    elif (n1 + n2) // 2 <= nx < n2 and (m1 + m2) // 2 <= ny < m2:
        answer += '4'
        # print("---------- check 4사분면 ---------")
        # print("nx : " + str(nx))
        # print("ny : " + str(ny))
        # print("(n1+n2)//2 : " + str((n1+n2)//2))
        # print("n2 : " + str(n2))
        # print("m1 : " + str(m1))
        # print("(m1+m2)//2 : " + str((m1+m2)//2)) 
        return check((n1 + n2) // 2, n2, (m1 + m2) // 2, m2)


d, number = input().split()

x, y = map(int, input().split())

# 사분면 초기 범위 변수 
n, m = 2**int(d), 2**int(d)

dx, dy = find(0, n, 0, m, 0) # 사분면 조각의 전표 각 좌표 시작, 끝 범위 , 인덱스 매개변수 지정
# print("dx : " + str(dx))
# print("dy : " + str(dy))
nx, ny = (-1*y) + dx, x + dy # 새로운 사분면 조각의 좌표

answer = ''

if 0 <= nx < n and 0 <=ny < m:
    print(int(check(0, n, 0, m)))
else:
    print(-1)