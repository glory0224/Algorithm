# 폰켓몬 문제 

# 당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다. 
# 홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
# 홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 
# 따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 
# 예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 이는 3번 폰켓몬 두 마리, 1번 폰켓몬 한 마리, 2번 폰켓몬 한 마리가 있음을 나타냅니다. 
# 이때, 4마리의 폰켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.



def solution(nums):
    # 중복을 제거한 폰켓몬 종류 개수
    num_types = len(set(nums))
    
    # print(num_types)
    
    # 선택할 수 있는 폰켓몬 종류 개수 최대값
    max_num_types = len(nums) // 2
    
    # print(max_num_types)
    
    # 최대 값이 더 작다면 최대값이 정답 
    return num_types if num_types < max_num_types else max_num_types

print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2