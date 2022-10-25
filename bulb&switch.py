# 백준 2138번 전구와 스위치 

"""
아이디어 

1. 첫번째 전구를 키는 케이스와 키지 않는 케이스로 나누는 것 

-> 첫번째 전구는 비교할 이전 전구가 없기 때문에 두가지 경우를 모두 확인한다.

2. 한번 지나간 전구는 다시 건드리지 않는 것

-> 한번 지나간 전구를 다시 건드린다고 불가능한게 가능해지지도 않고 횟수만 늘어나기 때문이다.
-> 그리디 분류 이유

3. 전구의 상태가 바뀌면 양옆 전구가 바뀌기 때문에 

    두번째 전구부터 시작해서 이전 전구의 상태가 희망하는 상태인지 확인하고 

    다르다면 스위치를 눌러 상태를 변경하는 것 

-> 이전 전구의 상태만 비교하는 것은 for문을 돌면서 어차피 다음 전구는 비교 하기 때문이다.
"""

N = int(input())
state = list(input()) 
hope = list(input())

# 첫번째 전구가 켜져있는 상태의 메소드 
def change_zero(light):
    cnt = 1
    light[0] = str(1 - int(light[0])) # 첫번째와 그 다음 전구 상태 변경 
    light[1] = str(1 - int(light[1]))
    
    # 이전과 비교해야하기 때문에 range는 1부터 시작 
    for i in range(1, len(light)):
        # 만들어주려는 전구모양과 일치하면 그대로 통과
        if light[i-1] == hope[i -1]:
            continue
        # 아니라면 cnt 증가하고 전구모양을 변경 
        else:
            cnt += 1
            
            light[i-1] = str(1 - int(light[i -1]))
            light[i] = str(1 - int(light[i]))
            if i < len(light) - 1: # 해당 길이를 벗어나지 않는 경우에만 다음 전구 변경 
                light[i+1] = str(1 - int(light[i+1]))
    
    if hope == light:
        return cnt 
    
    return 200002

# 처음에 전구가 켜져 있지 않는 경우 
def non_change_zero(light):
    cnt = 0
    # 따로 변경해주지 않고 바로 비교 
    
    for i in range(1, len(light)):
        if light[i -1] == hope[i-1]:
            continue
        else:
            cnt += 1

            light[i-1] = str(1 - int(light[i -1]))
            light[i] = str(1 - int(light[i]))
            if i < len(light) -1:
                light[i + 1] = str(1 - int(light[i + 1]))
                
    if hope == light:
        return cnt
    
    return 100002

cnt1 = change_zero(state[:])
cnt2 = non_change_zero(state[:])

ans = min(cnt1, cnt2)
if ans == 100002: # 첫번째 전구가 켜져있는 상태의 return 값인 200002과 min으로 비교했을 때 ans 값에 저장된 것이기 때문에 불가능한 경우에 해당하고 -1 출력 
    ans = -1
print(ans)
