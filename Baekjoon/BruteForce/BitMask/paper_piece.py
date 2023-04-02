# 백준 14391번 종이 조각

# https://lagooni.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%A2%85%EC%9D%B4-%EC%A1%B0%EA%B0%81-14391%EB%B2%88-Python-Bitmasking

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().rstrip())))
    
ans = []

for i in range(1 << n*m):
    total = 0
    
    # 가로 합 계산 
    for row in range(n):
        rowsum = 0
        for col in range(m):
            # idx는 2차원 행렬을 1줄로 만들었을 때의 인덱스
            idx = row * m + col
            #print("i의 값 : " + str(i) +"row 값 : " + str(row) + "m 값: " + str(m) + "col 값 : " + str(col) + "가로 합 계산 idx:", str(idx),)
            if i & (1 << idx) != 0:
                #print("shift left 1 : " , str(i & 1 << idx))
                rowsum = rowsum * 10 + paper[row][col]
                #print("0 아닐때 rowsum : " + str(rowsum))
            else:
                total += rowsum
                #print("0일때 rowsum : " + str(rowsum))
                rowsum = 0
        total += rowsum
        
    #세로합 계산 
    for col in range(m):
        colsum = 0
        for row in range(n):
            idx = row*m + col
            #print("i의 값 : " + str(i) +"row 값 : " + str(row) + "m 값: " + str(m) + "col 값 : " + str(col) + "세로 합 계산 idx:", str(idx),)
            if i & (1 << idx) == 0:
                colsum = colsum * 10 + paper[row][col]
                #print("0 일때 colsum : " + str(rowsum))
            else:
                total += colsum
                #print("0 아닐때 colsum : " + str(rowsum))
                colsum = 0
        total += colsum
    
    ans.append(total)

print(max(ans))
    

    
