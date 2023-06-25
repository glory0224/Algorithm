# N개의 최소공배수

# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
# 예를 들어 2와 7의 최소공배수는 14가 됩니다. 
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

import math

def find_lcm_arr(arr):

    # 배열의 첫번째 수를 최소 공배수로 놓고 시작
    lcm = arr[0]
    
    # 향상 for문으로 다음 배열 값부터 끝까지 돌면서
    for num in arr[1:]:
        # 최소 공배수와 배열 숫자의 최대공약수를 최소공배수와 배열 숫자로 곱한 값으로 나누면서 최소 공배수를 갱신한다.
        # print("before lcm : ", lcm)
        # print("num : ", num)
        lcm = lcm * num // math.gcd(lcm, num)
        # print("after lcm : ", lcm)
    return lcm


def solution(arr):

    return find_lcm_arr(arr)

print(solution([2,6,8,14]))
print(solution([1,2,3]))