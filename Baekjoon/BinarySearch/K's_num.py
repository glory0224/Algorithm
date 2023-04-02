# 백준 1300번 K번째 수

# 이진 탐색
# https://claude-u.tistory.com/449

# 가장 잘못된 방법은 직접 for문을 두 번 돌려 리스트를 만든 뒤, 오름차순 정렬하는 것

# 예를 들어 10 * 10에서 20보다 작거나 같은 수를 생각해보자.

# 1*1~1*10

# 2*1~2*10

# 3*1~3*6

# ...

# ...

# ...

# 10*1~10*2

# 위 수가 존재할텐데, 이는 반대로 생각해보면 20을 행으로 나눈 몫이다.

# 20//1: 10개 --> 단 열의 숫자(N*N배열이므로)를 초과할 수 없다.

# 20//2: 10개

# 20//3: 6개

# ...

# ...

# ...

# 20//10: 2개

# 따라서 이를 식으로 표기해보면 아래와 같다.

# temp = 0

# for i in range(1, N+1):
#         temp += min(mid//i, N)

# 이렇게 해당 숫자(mid)보다 작거나 같은 숫자들을 전부 찾아줌으로써 mid가 몇번째에 위치한 숫자인지 알아낼 수 있다.

# 이를 이분탐색으로 진행한다.


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, k

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n) # mid 이하의 i의 배수 or 최대 N : 배열의 크기가 N * N 열의 숫자를 초과할 수 없기 때문에 N보다 작아야만 값을 갱신 가능하다.
        # print(str(i) + "번째 temp : " + str(temp))
    # 이분 탐색 실행
    if temp >= k: # 찾고자 하는 수보다 temp가 크면 
        # print("start : " + str(start))
        # print("end : " + str(end))
        # print("mid : " + str(mid))
        answer = mid
        
        end = mid - 1
    else:
        # print("k가 temp보다 크거나 같을 때 start : " + str(start))
        # print("k가 temp보다 크거나 같을 때 end : " + str(end))
        # print("k가 temp보다 크거나 같을 때 mid : " + str(mid))
        
        start = mid + 1

print(answer)



