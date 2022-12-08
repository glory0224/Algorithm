# 백준 1561번 놀이 공원 문제 
# 이분 탐색
# https://jjangsungwon.tistory.com/96 
# pypy3 

# 문제 접근

# 1. N명의 아이들을 놀이기구에 태울 수 있는 시간을 구한 후 놀이기구의 번호를 구한다. 
# 2. N의 범위가 크기 때문에 0초부터 시간을 탐색하는 것이 아닌 이분탐색으로 시간을 구한다.

# 알고리즘

# 1. 놀이기구의 수보다 아이들의 수가 적으면 아이들의 수를 출력합니다. 
# 2. 이분 탐색을 통해 아이들을 모두 태울 수 있는 시간을 찾습니다. 
# 3. 구한 시간 - 1분까지 몇명의 아이를 태울 수 있는지 탐색합니다.
# 4. 구한 시간에 탑승하는 아이들을 계산하면서 제일 마지막에 탑승하는 놀이기구의 번호를 출력합니다.
# (놀이 기구 탑승 인원이 N명이 될 때의 놀이기구 번호를 출력하면 됩니다.)

import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    t_list = list(map(int, sys.stdin.readline().split()))

    if n < m: # 아이들보다 놀이기구가 작은 경우
        print(n)
    else:
        # 이분 탐색
        left, right = 0, 60000000000
        t = None
        while left <= right:
            # print("left : " + str(left))
            # print("right : " + str(right))
            mid = (left + right) // 2
            cnt = m # 기존 놀이기구 수(첫 탑승이기 때문에 해당 수만큼 인원수 추가)
            for i in range(m):
                # print("i : " + str(i))
                # print("mid : " + str(mid))                
                cnt += mid // t_list[i]  # 기존 놀이기구 수(첫 탑승이기 때문에 해당 수만큼 인원수 추가) + 놀이기구의 탑승 시간별 인원 수를 더해가면 mid분까지 탄 학생 수를 구할 수 있음 
                # print("cnt : " + str(cnt))
            if cnt >= n: # n명을 태울 수 있는 상황 (n명에 해당할 때까지 이분 탐색으로 전체 범위를 쪼개고 n명에 도달 했을 때 분을 t 변수에 저장)
                t = mid
                right = mid - 1
            else:
                left = mid + 1
        
        # t - 1에 탑승한 아이들의 숫자를 계산한다. 
        cnt = m # 처음 탑승 인원 
        # t - 1을 하는 이유 : 처음 놀이기구의 탑승한 인원인 m의 0분은 제외한 1분부터 계산해야 하기 때문이다.
        for i in range(m):
            cnt += (t - 1) // t_list[i] # t분까지 놀이기구를 탄 총 학생의 수 
            # print("t 결과 cnt : " + str(cnt))
        # t에 탑승한 학생을 계산한다.
        for i in range(m):
            if t % t_list[i] == 0: # t 시간에 탑승한 학생 수
                cnt += 1
            if cnt == n:
                print(i + 1) # index 0부터 시작했기 때문에 진짜 마지막 탑승 놀이기구 번호는 + 1
                break


