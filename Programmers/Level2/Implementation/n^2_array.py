# n^2 배열 자르기

# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 10^7
# 0 ≤ left ≤ right < n^2
# right - left < 10^5

# 범위가 크기 때문에 2차원 배열을 미리 선언하고 쪼개는 방법은 시간초과가 날 수 있다. 

# 1차원 배열만 생성하고 left, right 인덱스 범위의 값을 바로 채우는 방법으로 풀이

def solution(n, left, rigtht):
    answer = []

    for idx in range(left, rigtht+1):
        row , col = idx // n, idx % n
        answer.append(max(row, col)+1)

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))