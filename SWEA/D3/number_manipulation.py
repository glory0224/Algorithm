# 숫자 조작 문제

# 9자리 경우의 수를 찾기 때문에 브루트 포스 방식 사용 가능

# 최대 최소를 구하는 문제로 모든 경우의 수를 다 찾는다. 

# 9자리 이하의 음이 아닌 정수 N이 있다. 당신은 이 수에서 한 쌍의 숫자를 골라 그 위치를 바꾸는 일을 최대 한 번 하여(안 하거나, 한 번만 하여) 새로운 수 M을 만들 수 있다. 단, 바꾼 결과 M의 맨 앞에 ‘0’이 나타나면 안 된다.

# M의 최솟값과 최댓값을 구하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 하나의 줄로 이루어진다. 각 줄에는 0 이상 999,999,999 이하의 정수 N이 주어진다. N ≠ 0 이라면 주어지는 수가 0으로 시작하지 않는다.


# [출력]
# 각 테스트 케이스마다, M의 최솟값과 최댓값을 공백 하나를 사이로 두고 출력한다.

# 입력
# 4
# 12345
# 54321
# 142857
# 10000

# 출력
# #1 12345 52341
# #2 14325 54321
# #3 124857 842157
# #4 10000 10000

T = int(input())

for tc in range(1, T+1):
    # 문자열 형태로 입력 받는다. 
    nums = input()

    # 한 쌍의 숫자를 골라 바꾸기 때문에 이중 반복문을 사용해 최소 값을 만든다. 

    min_num = nums

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            
            # 인덱스가 첫 번째이고, 바꿀 숫자가 문자열 '0' 인 경우 continue
            if i == 0 and nums[j] == '0':
                continue

            # 입력받은 문자열을 리스트로 변환
            temp = list(nums)
            # 자리수를 변경하면서 min_num 갱신
            temp[i], temp[j] = temp[j], temp[i]
            
            # 파이썬은 문자열이 숫자인 경우 비교가 가능함
            if ''.join(temp) < min_num:
                min_num = ''.join(temp)
    
    max_num = nums

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # 인덱스가 첫 번째이고, 바꿀 숫자가 문자열 '0' 인 경우 continue
            if i == 0 and nums[j] == '0':
                continue
            
            temp = list(nums)

            temp[i], temp[j] = temp[j], temp[i]

            if ''.join(temp) > max_num:
                max_num = ''.join(temp)
    
    print(f"#{tc} {min_num} {max_num}")




