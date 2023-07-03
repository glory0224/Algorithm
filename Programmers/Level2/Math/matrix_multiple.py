# 행렬의 곱셈

# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.



# O(N^3)
# 이 문제를 단순 3중 반복 풀이법이 가능한 이유는 행과 열의 길이가 2 ~ 100 이기 때문

def solution(arr1, arr2):
    
    answer = []

    

    for i in range(len(arr1)):
        row = [] # arr1의 행의 길이만큼 초기화
        for j in range(len(arr1[0])): # arr2의 첫번째 행의 길이
            val = 0 # 각 지점의 정답
            for k in range(len(arr2)):
                # arr1을 arr2에 곱함
                val += arr1[i][k] * arr2[k][j]
            row.append(val)
        answer.append(row)

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3,3], [3, 3]])) # [[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4,2,4], [3,1,4]],[[5,4,3], [2, 4, 1], [3,1,1]])) # [[22, 22, 11], [36, 28, 18], [29, 20, 14]]