# 백준 로또 6603번 
#https://pacific-ocean.tistory.com/238


#8 1 2 3 5 8 13 21 34
#s배열에는 1, 2, 3, 5, 8, 13, 21, 34가 담긴다.
#dfs함수를 처음 쓰게 되면
#combi배열에는 차례대로 1, 2, 3, 5, 8, 13이 담기게 된다.
#depth가 6이기때문에 출력을 해주고 return하여 이전 함수로 돌아가게 된다.
#for 문의 i는 증가한 상태이므로 1, 2, 3, 5, 8, 21이 담기게 된다.



def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
combi = [0 for i in range(13)] # 인덱스의 해당하는 범위 수가  0 ~ 13까지 
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()
    
    
