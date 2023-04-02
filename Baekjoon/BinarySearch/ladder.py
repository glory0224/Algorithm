# 백준 2022번 사다리 문제 

# 삼각형의 닮음과 이분탐색을 이용한 문제 풀이

# 아래 두 블로그 참고하여 공부 

# https://dkrnfls.tistory.com/117
# https://jinho-study.tistory.com/687  

# h1 = sqrt(x**2 - width**2)
# h2 = sqrt(y**2 - width**2)

# 삼각형의 닮음 
# 너비에 해당하는 width를 

# w2 : c = w : h1 -> 내항곱 = 외항곱 -> wc = h1w2
# w1 : c = w : h2 -> 내항곱 = 외항곱 -> wc = h2w1

# w = w1 + w2 , w1의 값 : w1 = wc/h2 , w2의 값 : w2 = wc/h1

# w = (wc/h2) + (wc/h1)

# 1 =  (c/h2) + (c/h1) -> 통분 -> (h1 + h2)c / h1h2

# c = h1h2 / (h1+h2) -> 위의 식에서 각 변에 분모 분자의 역순을 곱하여 왼쪽과 같은 식으로 만든다.

# 위와 같은 수식을 토대로 get_c의 함수를 생성하고 이분 탐색으로 두 빌딩의 너비를 구한다.

# 문제에 절대/상대 오차는 10 ** -3 까지 허용하기 오차가 나오더라도 답으로 인정된다. 


import sys

input = sys.stdin.readline

# 삼각형의 닮음을 활용하여 c를 구하는 함수 
def get_c(x, y, width):
    h1 = (x**2 - width**2) ** 0.5
    h2 = (y**2 - width**2) ** 0.5
    c = h1 * h2 / (h1 + h2)
    return c

def ladder():
    x, y, c = map(float, input().split())
    start, end = 0, min(x, y)
    res = 0
    while (end - start) > 0.000001:
        width = (start + end) / 2
        res = width
        # c를 구했는데 기존의 c보다 같거나 크면 w값을 키워주어서 h1, h2의 값을 작게 해주어야 한다.(이분 탐색)
        if get_c(x, y, width) >= c: 
            start = width
            print("start : " + str(start))
        else:
            end = width
            print("end : " + str(end))
    print(res)

ladder()
