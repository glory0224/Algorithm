# 승률 비교하기

# 삼성 1:1 프로그래밍 리그의 시즌이 끝났다. 앨리스는 B전 A승, 밥은 D전 C승이다. 누구의 승률이 더 높은가?


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 네 자연수 A, B, C, D(1 ≤ A ≤ B ≤ 100, 1 ≤ C ≤ D ≤ 100)이 공백로 구분되어 주어진다.


# [출력]

# 각 테스트 케이스마다 앨리스의 승률이 더 높으면 “ALICE”, 밥의 승률이 더 높으면 “BOB”, 둘의 승률이 같으면 “DRAW”를 출력한다.

# [힌트]

# 첫 번째 Testcase를 예로 들면 엘리스는 2전 1승, 밥은 4전 2승이다.

# 엘리스의 승률은 1/2 밥의 승률은 2/4로 서로 같으므로 “DRAW”를 출력한다.

# 입력
# 3
# 1 2 2 4
# 4 5 2 5
# 1 9 5 6

# 출력
# #1 DRAW
# #2 ALICE
# #3 BOB


# 출력을 리스트로 변환해서 읽어오는 것도 관건

T = int(input())
answers = [] # 정답을 리스트에 담아두고 출력하는 방식으로 시간초과를 방지한다. 

for tc in range(1, T+1):

    A, B, C, D = map(int, input().split())

    

    if (A / B) == (C/D):
        answers.append(f"#{tc} DRAW")
    elif (A / B) > (C/D) :
        answers.append(f"#{tc} ALICE")
    elif (A / B) < (C/D) :
        answers.append(f"#{tc} BOB")

for x in answers:
    print(x)
        
