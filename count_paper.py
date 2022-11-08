# 백준 1780번 종이의 개수 문제
# 재귀 함수와 분할 정복을 이용한 문제 해결  

T = int(input())
N = []
zero = 0
one = 0
minus = 0

for i in range(T):
     N.append(list(map(int, input().split())))

#board = [list(map(int, input().split())) for _ in range(T)]

# print(N)
#print('-------------------------------')
#print(board)

# 재귀방식으로 (x, y)로부터 가로로 n개, 세로로 n개의 종이 개수를 확인하는 함수
def dfs(x, y, n):
    global zero, one, minus
    
    num_check = N[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 같은 수로 되어 있는지 확인, 아닐 때 부분 문제 호출 
            # 부분 문제 호출시 같은 수만 있을 경우는 아래 로직은 타지 않고 재귀로 호출한 부분 문제 범위의 dfs 함수만 돌고 종료한다. 
            if(N[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        # print("x : " + str(x))
                        # print("k : " + str(k))
                        # print("n : " + str(n))
                        # print(x+k*n // 3) # 연산 순서 : x+k , *n , // 3
                        # print("y : " + str(y))
                        # print("l : " + str(l))
                        # print("n : " + str(n))
                        # print(y+l*n//3)
                        # print("----------------------")
                        dfs(x+k*n // 3, y+l*n//3, n//3) 
                        # print("minus : " + str(minus))
                        # print("zero : " + str(zero))
                        # print("one : " + str(one))
                return
    
    # 부분 문제가 같은 수로 2차원 배열을 다 돌았을 경우 해당 개수 카운트           
    if num_check == -1:
        minus += 1
    elif num_check == 0:
        zero += 1
    else:
        one += 1

dfs(0,0,T)

print(f'{minus}\n{zero}\n{one}')