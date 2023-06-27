# 귤 고르기

# 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 

# 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.

# 예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.

# 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

def solution(k, tangerine):

    # 귤의 크기별로 개수를 담는 딕셔너리 생성
    tangerine_dict = {}

    for size in tangerine:
        # 딕셔너리 안에 값이 있는 경우 개수 추가
        if size in tangerine_dict:
            tangerine_dict[size] += 1 
        else: # 값이 없는 경우 개수 1개 넣기
            tangerine_dict[size] = 1
    
    print(tangerine_dict)

    # 각 크기의 값들을 리스트로 정렬해서 변경
    counts = sorted(tangerine_dict.values())

    print(counts)

    answer = 0 # 최소 종류

    # while문으로 counts의 맨 뒤 크기부터 빼주면서 최소값을 구한다.
    while 0 < k:
        k -= counts[-1]
        del counts[-1] # 빼줬으면 그 다음 값을 가져오기 위해 값을 삭제한다.
        answer += 1 # 종류 추가
    
    return answer



print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1

