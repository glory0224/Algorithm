# 할인 행사 문제

# 정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

# 제한사항
# 1 ≤ want의 길이 = number의 길이 ≤ 10
# 1 ≤ number의 원소 ≤ 10
# number[i]는 want[i]의 수량을 의미하며, number의 원소의 합은 10입니다.
# 10 ≤ discount의 길이 ≤ 100,000
# want와 discount의 원소들은 알파벳 소문자로 이루어진 문자열입니다.
# 1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12



from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    want_dict = dict()
    
    for key, val in zip(want, number):
        want_dict[key] = val
    
    for i in range(len(discount) - 9):
        # Counter 함수는 주어진 이터러블(리스트, 문자열 등)의 각 원소의 개수를 세는 데 사용되는 함수
        c = Counter(discount[i:i+10]) # 처음 시작일부터 10일차까지의 dict 저장
        # print(c)
        if c == want_dict: # 그 경우가 원하는 dict의 count와 동일하다면 정현이가 원하는 제품을 모두 할인 받을 수 있는 경우의 수로 + 1
            answer += 1
    
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
