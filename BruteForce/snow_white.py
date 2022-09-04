#백준 2309번 백설공주와 일곱 난쟁이 문제 

# 9명중 7명을 뽑게 되면 경우의 수가 굉장히 많아지기 때문에 역으로 9명중 2명만 뺀 값이 100인 경우로 구해본다. 

nan = []
for i in range(9):
    nan.append(int(input()))

# 오름차순 정렬
nan.sort()
            
sum_nan = sum(nan)

for i in range(len(nan)):
    for j in range(i+1, len(nan)):
        # 9명 난쟁이의 합계에서 이중 for문을 돌면서 2명 뺀 값이 100인 경우 
        if sum_nan - nan[i] - nan[j] == 100:
            # 뺄 두명의 난쟁이 키만 pass로 넘기고 나머지는 출력한다. 
            for k in range(len(nan)):
                if k == i or k == j:
                    pass
                else:
                    print(nan[k])
            exit() # i, j를 제외한 7명이 다 출력되었기 때문에 인덱스를 다 돌지 않고 코드를 종료시킨다.
            
