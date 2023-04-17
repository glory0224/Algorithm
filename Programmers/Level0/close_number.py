# 가까운 수 문제

# 문제 
# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

# 제한 사항
# 1 ≤ array의 길이 ≤ 100
# 1 ≤ array의 원소 ≤ 100
# 1 ≤ n ≤ 100
# 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.

# 입출력 예
# array = [3, 10, 28]	n = 20	result = 28
# array = [10, 11, 12]	n = 13	result = 12

def solution(array, n):
    # 가장 가까운 수 찾기
    answer = min(array, key=lambda x: abs(x - n))

    # 가장 가까운 수가 여러 개일 경우(절대값이 같음) 배열에 저장
    candidates = []
    for i in range(len(array)):
        if abs(array[i] - n) == abs(answer - n):
            candidates.append(array[i])
    
    # 배열에 값이 있다는 건 가장 가까운 수가 여러개 아니면 가장 가까운 수 출력
    if candidates:
        return min(candidates)
    else:
        return answer
    
print(solution([3, 10, 28], 20))