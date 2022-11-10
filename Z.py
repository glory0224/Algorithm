# 백준 1074번 z 문제 
# https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-1074-Z

"""
아이디어 

찾아야 하는 좌표의 행렬이 주어지기 때문에 전체 매트릭스에서 해당 좌표가 어느 사분면에 있는지 계산하며 찾아가는 방식 적용

1. N은 최대 탐색 횟수가 되며 Z 순서로 2사분면, 1사분면, 3사분면, 4사분면 순으로 탐색하며 해당 사분면을 기준으로 좌표 수정 

2. 시작인 2사분면의 경우 좌표를 따로 수정하지 않아도 된다. 

3. 1사분면은 c를 크기만큼 빼주어 좌표를 수정해준다. 또한 2사분면으로 이동하기 위해서 1사분면에 해당하는 갯수만큼 이동해야 하므로 size ** 2를 더해준다. 

4. 3사분면은 r을 크기만큼 빼주어 좌표를 수정해준다. 또한 2사분면으로 이동하기 위해선 2, 1 사분면에 해당하는 갯수만큼 이동해야 하므로 size ** 2를 더해준다.

5. 4사분면은 r과 c를 크기만큼 빼주어 좌표를 수정해준다. 또한 4사분면으로 이동하기 위해선 2, 1, 3 사분면에 해당하는 갯수 만큼 이동해야 하므로 size ** 2를 3번 더해준다. 
"""

N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2
        # print("1사분면 : " + str(cnt))
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        # print("3사분면 : " + str(cnt))
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        # print("4사분면 : " + str(cnt))
        r -= size
        c -= size
    N -= 1

# while문의 False 조건일 때 아래 if문 적용 

if r == 0 and c == 0: # z순서에 따라 2사분면은 좌표를 따로 수정하지 않음 
    print(cnt)
if r == 0 and c == 1: # 1사분면은 
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)