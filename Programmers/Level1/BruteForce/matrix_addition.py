# 행렬의 덧셈

def solution(arr1, arr2):

    answer = []

    for row1, row2 in zip(arr1, arr2):
        tmp_list = [] # 값을 넣어줄 리스트 
        
        for i in range(len(row1)): # 길이가 같다고 했으므로 하나의 row 기준을 잡는다.
            tmp_list.append(row1[i] + row2[i])
        
        answer.append(tmp_list)
    
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))


