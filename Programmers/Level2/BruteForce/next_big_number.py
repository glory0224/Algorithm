# 다음 큰 숫자

# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

def solution(n):
    answer = 0
    big_n = n # 증가할 수
    bin_n = bin(n)[2:] # n의 이진수

    while True:
        big_n += 1 # n부터 1씩 증가
        if bin(big_n)[2:].count('1') == bin_n.count('1'): # 조건 2가 맞다면 n 다음 큰 수 중에서 제일 작은 수의 조건 1도 성립함
            answer = big_n
            return answer

print(solution(78)) # 83
print(solution(15)) # 23