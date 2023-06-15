# 정수 내림차순

# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    answer = 0

    str_n = str(n) # 문자열로 변환

    str_list = list(str_n) # 각각의 문자를 리스트에 담는다.

    # 내림차순 정렬
    str_list = sorted(str_list, reverse=True)

    # 정수로 형변환
    answer = int(''.join(str_list))

    return answer

print(solution(118372)) # 873211

