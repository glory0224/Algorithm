# 영준이와 신비한 뿔의 숲

# 유니콘과 트윈혼의 수 도출 문제

T = int(input())

for tc in range(1, T+1):
    # N : 뿔 개수 , M : 동물 수
    # 뿔이 2개와 1개이기 때문에 총 마릿수와 총 뿔 갯수 차이가 트윈혼의 마릿수가 됩니다.
    N, M = map(int, input().split())

    unicorn = M - (N - M)
    twin = N - M

    print(f"#{tc} {unicorn} {twin}")