# 영준이의 카드 카운팅 - 문자열 처리

# 최근 영준이는 카드 게임에 꽂혀 있다.

# 영준이가 하는 카드 게임에는 한 덱의 카드가 필요한데 여기서 얘기하는 “한 덱”이란 스페이드, 다이아몬드, 하트, 클로버 무늬 별로 각각 A, 2~10, J, Q, K의 라벨 즉 4개의 무늬 별로

# 각각 13장씩 총 52장의 카드가 있는 모음을 의미한다.

# 편의상 A는 1, J, Q, K는 11, 12, 13으로 하여 1~13의 숫자가 카드에 적혀있다고 하자.

# 영준이는 몇 장의 카드를 이미 가지고 있는데 게임을 하기 위해서 몇 장의 카드가 더 필요한지 알고 싶어 한다.

# 그리고 이미 겹치는 카드를 가지고 있다면 오류를 출력하고자 한다.

# 지금 가지고 있는 카드의 정보가 주어지면 이 작업을 수행하는 프로그램을 작성하라.


# [입력]

# 맨 위 줄에 테스트케이스의 개수가 주어진다.

# 각 테스트케이스 별로 순서대로 첫 번째 줄에 지금 영준이가 가지고 있는 카드에 대한 정보 S (1 ≤ |S| ≤ 1000)가 주어진다.

# S는 각각 3자리로 표현되는 카드들의 정보를 붙여서 만든 하나의 문자열인데 각 카드는 TXY 꼴로 표현되며,

# T는 카드의 무늬(S, D, H, C)이며 XY는 카드의 숫자 (01 ~ 13)이다.

# [출력]

# 각 테스트케이스 별로 순서대로 한 줄씩 답을 출력하는데, 문자열 S를 보고 지금 무늬 별로(S, D, H, C 순서로) 몇 장의 카드가 부족한지 출력하여라.

# 이미 겹치는 카드가 있다면 문자열 “ERROR” (쌍따옴표는 출력하지 않는다)를 출력한다

# 입력
# 3
# S01D02H03H04
# H02H10S11H02
# S10D10H10C01

# 출력
#1 12 12 11 13 	// Test Case 1의 정답
#2 ERROR // Test Case 2의 정답
#3 12 12 12 12 // Test Case 3의 정답


T = int(input())

for tc in range(1, T+1):
    cards = input()

    cards_cnt = {
        'S' : 13,
        'D' : 13,
        'H' : 13,
        'C' : 13
    }


    # cards의 길이만큼 반복문 실행 - 문자와 숫자 2자리까지 구분해야하기 때문에 인덱스를 3씩 증가
    for i in range(0, len(cards), 3):
        # 카드 모양
        card = cards[i]
        # 카드 숫자
        num = cards[i+1:i+3]
        # 저장해둔 카드 모양과 숫자 정보가 cards에 똑같이 있는 경우
        if card+num in cards[i+3:]:
            print(f"#{tc} ERROR") # ERROR 출력 후 종료
            break
        else: # 해당 문양의 카드 개수 차감
            cards_cnt[card] -= 1
    
    else: # 종료 되지 않고 for문이 마무리 된 경우
        print(f"#{tc} {cards_cnt['S']} {cards_cnt['D']} {cards_cnt['H']} {cards_cnt['C']}")


