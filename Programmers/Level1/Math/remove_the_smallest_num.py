# 제일 작은 수 제거하기

def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    
    if not arr:
        arr.append(-1)
        return arr
    else:
        return arr
    
print(solution([4,3,2,1]))
print(solution([10]))