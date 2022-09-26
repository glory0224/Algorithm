#백준 1182번 부분 수열의 합 

# 백트레킹 재귀 함수로 풀기 
# https://seongonion.tistory.com/98


import sys

input = sys.stdin.readline

n , s = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0

def subset_sum(idx, sub_sum):
    
    # idx가 증가되도 cnt가 누적가능하게 전역변수 설정 
    global cnt
    
    if idx >= n:
        return
    
    # 배열의 값을 더해준다.
    sub_sum += arr[idx]
    
    # 주어진 s와 같다면 cnt 1 증가 
    if sub_sum == s:
        cnt += 1
    
    # 현재 arr[idx]를 선택한 경우의 가지 
        
    subset_sum(idx+1, sub_sum)
    # print("현재 idx 선택 : " + str(idx))
    # print("현재 arr 선택 : " + str(arr[idx]))
    # print("현재 arr[idx] 선택 : " + str(sub_sum))
    
    # 현재 arr[idx]를 선택하지 않은 경우의 가지 
    
    subset_sum(idx+1, sub_sum - arr[idx])
    # print("-----------------------------------------")
    # print("현재 idx 선택 안함 : " + str(idx))
    # print("현재 arr 선택 안함 :" + str(arr[idx]))
    # print("현재 arr[idx] 선택 안함 :" + str(sub_sum))
    
subset_sum(0, 0)
print(cnt)
    