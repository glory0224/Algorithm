# 숫자 짝꿍

# 그리디 + 문자열 활용 문제(딕셔너리)


# 문제 입출력 예시는 통과했으나 테스트 케이스 일부는 통과하지 못한 코드

# def solution(X, Y):
#     answer = ''
#     common_values = set(X) & set(Y)  # 두 문자열의 교집합을 구함
#     extracted_values = []

#     for value in common_values:
#         count1 = X.count(value)  # X에서 value의 개수를 세기
#         count2 = Y.count(value)  # Y에서 value의 개수를 세기
#         extracted_values.extend([value] * min(count1, count2))  # 최소 개수만큼 value를 추출하여 리스트에 추가
    
#     # 일치하는 값이 없을 때
#     if not extracted_values:
#         answer += '-1'
#     else:
#         if extracted_values[0] == '0':  # 첫 번째 값이 0이라면
#             answer += '0'
#         else:
#             answer += ''.join(map(str, sorted(extracted_values, reverse=True)))
                
#     return answer

# 개선된 답변

def count_numbers(number:str):
    count_dict = {n:0 for n in "9876543210"} # 내림차순으로 dict 선언
    
    # 매개변수 number를 받고 number가 count_dict 안에 있으면 키 값의 벨류 증가
    for num in number:
        count_dict[num] += 1 # 해당하는 키에 cnt 증가
    
    return count_dict
    

def solution(X, Y):
    answer = ''

    # 딕셔너리를 이용한 각 문자열 타입의 숫자 개수 카운트 함수 사용
    X_count_dict = count_numbers(X)
    Y_count_dict = count_numbers(Y)

    # 높은 수부터 넣어줘야 최대 값이 나오기 때문에 문자열 내림차순 선언
    for num in "9876543210":
        
        # 비교하는 숫자가 0 이고 answer의 첫번 째로 들어갈 때
        if num == "0" and answer == "":
            # 최소 개수가 1개인 경우
            if min(X_count_dict[num], Y_count_dict[num]):
                return '0'
            # 최소 개수가 1개가 아닌 경우
            else:
                return '-1'

        answer += num * min(X_count_dict[num], Y_count_dict[num])

    return answer

print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))

