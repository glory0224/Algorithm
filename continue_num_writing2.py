# 백준 1790번 수 이어쓰기 2

# https://yeoooo.github.io/algorithm/BOJ1790/


# 입력 N 기준 최대 10억, 시간 제한은 7초
# 이어쓰기 방식으로 하면 시간이 부족함

# 이분 탐색을 이용한다. 

# 먼저 k가 1 ~ 9의 범위 안에 있다면 자리수는 한자리이다. k가 10 ~ 99의 범위 안에 있다면 자리수는 두자리이다. 
# 위와 같이 k에서 자리수에 자리수를 늘려가며 맞게끔 9 x 1, 90 x 2, 900 x 3 ... 을 빼준다.
# 이유는 1 ~ 9는 각 숫자마다 1자리씩이지만 10 ~ 99부터는 각 숫자마다 2자리 이상이기 때문이다. 

# k에서 자리수에 맞게 빼주다 보면 더 이상 뺄 수 없는 값이 나온다. 
# 이 때 k가 어느 수에 속하는지 알기 위해 k를 지금까지 세어온 자리 수 만큼으로 나눈 뒤 
# 그 값을 더해준다. (k가 300인 경우 그 자리수인 3으로 나눠주면 원하는 값이 100) k로 원하는 수를 찾았으면 n과 대소비교 후 값을 낸다.  


# cf) 10~99, 100~999 … 사이의 값은 89개가 아닌 90개이다.

import sys 

input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0
digit = 1 # 자리수 
nine = 9 # 9까지 범위 

while k > digit*nine:
    k = k - (digit * nine) # 자리수를 늘려가면서 k에서 빼주기 
    ans = ans + nine
    digit += 1
    nine = nine * 10
    # print("ans : " + str(ans))
    # print("digit : " + str(digit))
    # print("nine : " + str(nine))
    # print("k : " + str(k))




ans = (ans+1) + (k-1) // digit # 연산 순서가 // 우선 그다음 + 
# print("ans : " + str(ans))


if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit]) # ans는 int형으로 16인데 str로 형변환 후 [(k-1)%digit : 1] , 즉 1번째 인덱스인 '6'이 나온다. 파이썬 문법
    
        

