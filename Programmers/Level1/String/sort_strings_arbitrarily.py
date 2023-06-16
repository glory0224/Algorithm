# 문자열을 마음대로 정렬

# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):

    answer = []

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # 문자 담을 dict
    str_dict = dict()

    for str in strings:
        # 처음 딕셔너리에 해당 단어가 없는 경우 
        # 해당 키를 만들고 값으로 배열의 str를 보관 
        if str[n] not in str_dict:
            str_dict[str[n]] = [str] 
        else:
            # str_dict에 이미 존재하는 키라면 해당 키에 str을 추가합니다. 
            # case ["abce", "abcd", "cdx"], 2 경우 c, c, x 로 c가 중복되는데 이때 키 'c'의 리스트에 'c' : ["abce", "abcd"] 이와 같은 식으로 저장하기 위한 구문
            str_dict[str[n]].append(str)

    # print("str_dict : ", str_dict)
    
    for key in sorted(str_dict): # 오름차순 정렬된 키를 하나씩 가져와서
        answer.extend(sorted(str_dict[key])) # 키의 값이 오름차순 정렬된 상태인 각 키의 리스트 값을 asnwer 리스트로 옮길 때 , extend라는 리스트 함수를 이용해서 리스트에서 리스트로 옮긴다.
    
    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))