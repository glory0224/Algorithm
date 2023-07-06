# 의상 문제

# 코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

# 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

# 코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

def solution(clothes):
    answer = 0
    # 같은 이름을 가진 의상은 존재하지 않습니다.
    fashion_dict = dict() 
    
    for cloth, category in clothes:
        
        if category in fashion_dict: # 종류가 딕셔너리에 존재하면
            fashion_dict[category] += 1
        else:
            fashion_dict[category] = 1 # 아니면 종류가 1개이므로 1로 초기화
    
    
    # print(fashion_dict)
    answer = 1 # answer에 곱할 것이기 때문에 1로 초기화
    for category in fashion_dict.keys():
        # 내가 가진 옷 중에 입는 경우와 입지 않는 경우를 모두 곱해준다.
        # 아래는 (옷 종류 개수) + (옷을 입지 않는 경우 1가지) 해서 1을 더한 값을 곱해서 경우의 수를 구한다. 
        answer *= fashion_dict[category] + 1
    # 코니는 하루에 최소 한 개의 의상은 입습니다.
    # 전체 경우의 수에서 한 개도 입지 않고 나가는 경우의 수 1 빼기
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))