# 백준 3085번 사탕 게임 문제 
# 인접한 사탕색깔이 같지 않은 두 사탕을 교환 한 후에 사탕의 최대길이만큼 먹는다. 

# 행 기준이든 열 기준이든 최대로 많이 먹는 경우를 생각한다. 


T = int(input())


colors_str = []


for i in range(T):
    # map을 사용해서 각각 str로 쪼개준다. 
    colors = list(map(str, input()))
    colors_str.append(colors)
#print(colors_str)

# 최대 사탕 개수 초기화 
maxCount = 0 


# 배열의 행마다 같은 색 사탕을 계산하는 함수 
def width():
    # 전역변수로 최종 결과 값을 사용하기 위해 global 선언 
    global maxCount 
    
    for k in range(T):
        countRow = 1 #열의 초기 개수를 1로 
        for l in range(T-1): # index 0부터 시작하기 때문에 T-1
            
            if colors_str[k][l] == colors_str[k][l + 1]: # 만약 같은 열의 사탕의 색이 같다면 
                
                countRow += 1 # 열 카운트 늘려주기 
                maxCount = max(maxCount, countRow)
            else:
                countRow = 1 # 열 카운트를 다시 초기화 시켜준다. 
                
# 배열의 열마다 같은 색의 사탕이 몇개 있는지 계산하는 함수 
def height():
    for k in range(T):
        # 전역변수로 최종 결과 값을 사용하기 위해 global 선언 
        global maxCount
        
        countColumn = 1 #초기 개수를 1로 초기화
        for l in range(T - 1):
            if colors_str[l][k] == colors_str[l + 1][k]: #만약 같은 행의 사탕의 색이 같다면
                countColumn += 1 #사탕 개수를 1개씩 증가시켜주고
                maxCount = max(maxCount,countColumn) #증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else: #만약 같은 행의 색이 다르다면
                countColumn = 1 #개수를 1로 초기화                        
        
for i in range(T):
    for j in range(T - 1):
        # 만약 입력 받은 배열의 행의 원소가 다르다면        
        if colors_str[i][j] != colors_str[i][j + 1]:
            colors_str[i][j], colors_str[i][j + 1] = colors_str[i][j + 1], colors_str[i][j]
            width()
            height()
            colors_str[i][j + 1], colors_str[i][j] = colors_str[i][j], colors_str[i][j + 1]
        # 만약 입력 받은 배열의 열의 원소가 다르다면
        if colors_str[j][i] != colors_str[j + 1][i]:
            colors_str[j][i], colors_str[j + 1][i] = colors_str[j + 1][i], colors_str[j][i]
            width()
            height()
            colors_str[j + 1][i], colors_str[j][i] = colors_str[j][i], colors_str[j + 1][i]

print(maxCount) #색이 같은 사탕개수 최대값을 출력


# 예제 입력 1로 2차원 배열을 표로 정리

#      0  | 1 |  2  <- width 함수는 k 가 0 고정, 아래로 + 1 씩 증가하면서 같은 열의 색깔이 같은지 여부 확인 
#   0  C  | C |  P 
#   1  C  | C |  P
#   2  P  | P |  C
#   ↑ height 함수는 k가 이쪽이 0으로 고정, 오른쪽으로 + 1 씩 증가하면서 같은 행의 색깔이 같은지 여부 확인


        
