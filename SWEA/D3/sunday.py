

T = int(input())

for tc in range(1, T+1):

    day = input().strip()
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    if day == 'SUN':
        cnt = 7
    else:
        cnt = 0
        for i in range(len(days)):
            if days[i] == day:
                while days[i] != 'SUN':
                    i += 1 # 인덱스를 변경하면서
                    cnt += 1 # cnt 증가

    print(f"#{tc} {cnt}")