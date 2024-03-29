# 몬스터 사냥 문제 

# 용사가 몬스터를 공격할 때는 기본적으로 D만큼의 데미지를 입힌다. 여기에, 용사가 익힌 공격의 레벨 L에 따라 추가적인 데미지가 있는데,

# 지금까지 몬스터를 때린 횟수가 n번이라고 하면, 다음 공격이 몬스터에게 입히는 데미지는 D(1+nㆍL%)가 된다. %는 1/100을 의미한다.
# 지금까지 용사가 몬스터를 때린 횟수가 0번이라고 할 때, 앞으로 총 N번의 공격을 하면 몬스터에게 가한 총 데미지가 몇이 되는지 구하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 정수 D, L, N(102 ≤ D ≤ 104, 0 ≤ L ≤ 100, 1 ≤ N ≤ 102)이 공백 하나로 구분되어 주어진다. D는 100의 배수로만 주어진다.


# [출력]

# 각 테스트 케이스마다 용사가 몬스터에게 가한 총 데미지를 출력한다.

# 입력
# 3
# 100 0 1
# 200 12 10
# 10000 100 100

# 출력
# #1 100
# #2 3080
# #3 50500000

# 입력받는 레벨에 따라 추가 데미지를 더해주면서 총 가한 데미지 계산

T = int(input())

for tc in range(1, T+1):

    D, L, N = map(int, input().split())

    # 총 데미지
    damage = 0

    for n in range(N):
        damage += D * (1 + n * L * 1/100)
    
    print(f"#{tc} {int(damage)}") # int 형변환으로 나머지 소수점 자름