# 같은 숫자는 싫어

# 배열 arr가 주어집니다. 
# 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.

def solution(s):

    ans = []

    for i in s:
        # ans의 맨 뒤의 값이 현재 꺼낸 값과 동일한 경우 넣지 않는다.
        if ans[-1:] == [i]:
            continue

        ans.append(i)
    
    return ans

print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # 	[4,3]



