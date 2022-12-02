# 백준 13397번 구간 나누기 2
# 이분 탐색
# https://lkitty0302.tistory.com/10 


import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

def isVaild(midValue):
    global result
    low = nums[0]
    high = nums[0]
    d = 1

    for i in nums:
        # print("i : " + str(i))
        # print("high : " + str(high))
        # print("low : " + str(low))
        if high < i:
            high = i
        
        if low > i:
            low = i

        if high - low > midValue:
            d += 1
            low = i
            high = i
            # print("midValue : " + str(midValue))
            # print("midvalue보다 높은 경우 low : " + str(low))
            # print("midvalue보다 높은 경우 high : " + str(high))
    # print("d: " + str(d))
    # print("m >= d : " + str(m >= d))
    return m >= d 

start , end = 0, max(nums)


result = end

while(start <= end):
    mid = (start+end) // 2

    if isVaild(mid):
        end = mid - 1
        # print("result : " + str(result))
        result = min(result, mid)
    else:
        start = mid + 1

print(result)