# 백준 11726번 
T = int(input())

# dp 리스트 공간 확보 
d = [0] * (T + 1)

if T <= 3:
    print(T)
else:
    d[1] = 1
    d[2] = 2
    for i in range(3, T + 1):
        d[i] = d[i - 1] + d[i - 2]

    # 출력 답에 10007로 나눈 나머지 출력
    print(d[i] % 10007)
