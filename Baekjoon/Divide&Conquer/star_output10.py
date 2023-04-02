# 백준 2447번 별찍기 10
# https://study-all-night.tistory.com/5

# 별을 찍는 재귀 함수 (2차원 배열 1과 0 활용)

def draw_star(n):
    global Map # 재귀 함수 목적 전역변수 

    # 크기 3의 패턴 
    if n == 3:
        # 2차원 배열에서 1은 별이 찍힌것으로 0은 별이 안찍히는 것으로 
        Map[0][:3] = Map[2][:3] = [1]*3 # *** 
        
        Map[1][:3] = [1, 0, 1] # * * (가운데 별 안찍힘)
        return

    a = n // 3
    # print("a : " + str(a))
    # print("n : " + str(n))
    draw_star(n//3)
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: # 가운데 큰 3 패턴 구멍을 안찍기 위한 분기문
                continue
            for k in range(a): 
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] 
                

N = int(input())

# 메인 데이터 2차원 배열 
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map:
    for j in i :
        if j : # j == 1 true 값으로 별 찍기 
            print("*", end="")
        else: # j == 0 false 값으로 안찍음 
            print(" ", end="")
    print() # 개행을 위한 print
