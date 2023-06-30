# 멀리 뛰기

# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 
# 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

# 1번째 칸에 도달하는 방법의 수 : 1 (시작 지점)
# 2번째 칸에 도달하는 방법의 수 : 2 (1칸 뛰는 방법, 2칸 한번에 뛰는 방법)
# 3번째 칸에 도달하는 방법의 수 : 3(1+2)
# 4번째 칸에 도달하는 방법의 수 : 5(2+3)


# 점화식 도출
# n번째 칸에 도달하는 방법의 수는 (n-1번째 칸 도달 방법 수) + (n-2번째 칸 도달 방법 수)

def solution(n):

    fibo = [0, 1]

    for i in range(2, n+2):
        fibo.append((fibo[i-1] + fibo[i - 2]) % 1234567) # 점화식 :  n번째 칸에 도달하는 방법의 수는 (n-1번째 칸 도달 방법 수) + (n-2번째 칸 도달 방법 수)
    
    print(fibo)

    return fibo[n+1] # 칸의 마지막에 담기는 값이 n개의 끝 칸에 도달하는 경우의 수

print(solution(4)) # result = 5
print(solution(3)) # result = 3
