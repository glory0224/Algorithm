# 백준 12970번 AB 문제 
# 그리디 알고리즘 
# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-12970%EB%B2%88-AB

"""
아이디어

- 문자열 s는 B로 n만큼 채워서 초기화 한다.

- 오른쪽 기준 두번째부터 A를 넣는데, 끝에 넣는 경우는 쌍이 0개이기 때문에 두번째부터 넣는다. 

- 방법은 두가지로 나눌 수 있다.(if)

1. A를 앞으로 밀어내는 방법

2. A를 하나 추가하는 방법 

- curk의 값이 k가 되었을 때, while문을 종료하고 문자열을 출력한다.

- A를 추가하는 인덱스(n - 1 - (acnt + 1))에 이미 A가 존재하면 N개의 문자로 K라는 값에 도달하지 못했기 때문에 break

- 만약 while문 종료 후 curk 값이 k와 다르다면 문자열을 만들 수 없기 때문에 -1


"""

n , k = map(int, input().split())

def solve(n, k):
    s = list('B' * n)
    # acnt : A의 개수 0 초기화
    # curk : 반복 후 k 쌍의 개수 0 초기화
    # lidx : lastAIndex , 마지막 A의 인덱스 -1
    acnt, curk, lidx = 0, 0, -1
    
    while curk < k: 
        # if분기 별로 s배열을 계속 변형시킨다. 
        if lidx <= acnt -1: # A를 추가하는 경우 
            if s[n - 1 - (acnt + 1)] == 'A':
                break
            
            s[n - 1 - (acnt + 1)] = 'A'
            # print(s)
            lidx = n - 1 - (acnt + 1)
            acnt += 1
            curk += 1
        else: # A를 앞으로 미는 경우 
            s[lidx] = 'B'
            # print(s)
            s[lidx - 1] = 'A'
            # print(s)
            lidx -= 1
            curk += 1
            
    return s if curk == k else '-1' # 입력받은 쌍의 개수와 동일하면 s 반환, 만들 수 없는 경우라면 -1 반환 

answer = solve(n, k)
print(*answer, sep='') # 배열 값을 공백없이 출력하는 파이썬 문법


