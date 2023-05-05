# 상호의 배틀필드 문제

# 상호는 전차로 시가전을 하는 것을 테마로 한 새로운 게임 “배틀 필드”를 개발하기로 했다.

# 그래서 먼저 간단하게 프로토 타입 게임을 만들었다.

# 이 프로토 타입에서 등장하는 전차는 사용자의 전차 하나뿐이며, 적이나 아군으로 만들어진 전차는 등장하지 않는다.

# 사용자의 전차는 사용자의 입력에 따라 격자판으로 이루어진 게임 맵에서 다양한 동작을 한다.

# 다음 표는 게임 맵의 구성 요소를 나타낸다.
 
# 문자	의미
# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)
# 다음 표는 사용자가 넣을 수 있는 입력의 종류를 나타낸다.
 
# 문자	동작
# U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
# 전차가 이동을 하려고 할 때, 만약 게임 맵 밖이라면 전차는 당연히 이동하지 않는다.

# 전차가 포탄을 발사하면, 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진한다.

# 만약 포탄이 벽에 부딪히면 포탄은 소멸하고, 부딪힌 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지가 된다.

# 강철로 만들어진 벽에 포탄이 부딪히면 아무 일도 일어나지 않는다.

# 게임 맵 밖으로 포탄이 나가면 아무런 일도 일어나지 않는다.

# 초기 게임 맵의 상태와 사용자가 넣을 입력이 순서대로 주어질 때, 모든 입력을 처리하고 나면 게임 맵의 상태가 어떻게 되는지 구하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 두 정수 H, W (2 ≤ H, W ≤ 20) 이 공백으로 구분되어 주어진다.

# 이는 게임 맵의 높이가 H, 너비가 W임을 나타낸다.

# 즉, 게임 맵은 H x W크기의 격자판이다.

# 다음 H개의 각각의 줄에는 길이가 W인 문자열이 주어진다.

# 각각의 문자는 위의 게임 맵 구성 요소 표에 있는 문자들만 포함하며, 전차는 단 하나만 있다.

# 다음 줄에는 사용자가 넣을 입력의 개수를 나타내는 정수 N(0 < N ≤ 100) 이 주어진다.

# 다음 줄에는 길이가 N인 문자열이 주어진다.

# 각각의 문자는 위의 사용자가 넣을 수 있는 입력의 종류를 나타내는 표에 있는 문자들만 포함된다.


# [출력]

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 칸을 띄운 후, 모든 입력을 처리하고 난 후의 게임 맵을 H개의 줄에 걸쳐 출력한다.

# 입력
# 1
# 3 7
# ***....
# *-..#**
# #<.****
# 23
# SURSSSSUSLSRSSSURRDSRDS

# 출력
# #1 **....v
# .-..#..
# #......

T = int(input())

for tc in range(1, T+1):
    h, w = map(int, input().split())
    game_map = [list(input().strip()) for _ in range(h)]

    # 동서남북 이동 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 전차 방향
    directions = ['^', 'v', '<', '>']

    # 맵을 돌면서 전차 위치 확인
    for i in range(h):
        for j in range(w):
            if game_map[i][j] in directions: # 전차 방향이 있으면 해당 좌표 뽑기
                tank_x, tank_y = i, j
                tank_dir = directions.index(game_map[i][j]) # 전차 인덱스 넣기

    n = int(input()) # 명령어 개수 입력받기

    commands = input().strip() # 이동과 발사 명령어 받기

    # 커맨드 명령마다 전차 이동시키기

    for cmd in commands:
        if cmd == 'U': # 만약 이동 방향 명령어가 U이면 원래 있던 tank_dir 방향을 돌려준다.
            tank_dir = 0
            # 이동할 방향 좌표 지정
            nx, ny = tank_x + dx[tank_dir] , tank_y + dy[tank_dir]
            # nx, ny 에 대한 범위 확인
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == '.':
                game_map[tank_x][tank_y] = '.' # 원래 있던 자리에는 이동 표시
                tank_x, tank_y = nx, ny # 탱크 이동
            
            game_map[tank_x][tank_y] = directions[tank_dir] # 새로운 위치 이동
            
        elif cmd == 'D': # 이동 명령어 D
            tank_dir = 1
            # 이동할 방향 좌표 지정
            nx, ny = tank_x + dx[tank_dir], tank_y + dy[tank_dir]
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == '.':
                # 원래 자리는 통과표시 = '.'
                game_map[tank_x][tank_y] = '.'
                # 좌표 이동
                tank_x, tank_y = nx, ny
            # 해당 좌표에 탱크 놓기
            game_map[tank_x][tank_y] = directions[tank_dir]
        
        elif cmd == 'L':
            tank_dir = 2
            nx, ny = tank_x + dx[tank_dir] , tank_y + dy[tank_dir]
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == '.':
                game_map[tank_x][tank_y] = '.'
                tank_x, tank_y = nx, ny
            
            game_map[tank_x][tank_y] = directions[tank_dir]
        
        elif cmd == 'R':
            tank_dir = 3
            nx, ny = tank_x + dx[tank_dir], tank_y + dy[tank_dir]
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == '.':
                game_map[tank_x][tank_y] = '.'
                tank_x, tank_y = nx, ny
            
            game_map[tank_x][tank_y] = directions[tank_dir]
        
        elif cmd == 'S':
            nx, ny = tank_x, tank_y

            while True:

                nx, ny = nx + dx[tank_dir], ny + dy[tank_dir]

                # nx, ny의 범위가 벗어나면 종료
                if not (0 <= nx < h and 0 <= ny < w):
                    break

                if game_map[nx][ny] == '*':
                    game_map[nx][ny] = '.' # 파괴 후 초기화
                    break
                elif game_map[nx][ny] == '#': 
                    break # 못부수니 종료 
    
    print(f"#{tc} ", end='')
    for i in range(h):
        print(''.join(game_map[i])) # 행만큼 출력
                    






