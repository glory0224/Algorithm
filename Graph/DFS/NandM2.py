# 백준 15650번 문제 

# N&M과 유사한 문제 - [1, 2] , [2, 1] 경우를 중복으로 보고 오름차순인 [1,2]만 출력 
 


n, m = list(map(int, input().split()))

seq = []

# 매개 변수로 start 변수 추가 
def dfs(start):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return

          
    for i in range(start, n+1):
        # 여기서 if문 조건을 걸어준다면 dfs(i)로 작성 
        
        if i not in seq:
            seq.append(i)
            dfs(i)  
            seq.pop()
        
        # 만약에 여기 if문의 조건을 삭제하고 코드를 작성한다면 dfs(i+1)로 작성하는 방법도 있다.         
            # seq.append(i)
            # dfs(i+1)  
            # seq.pop()
            
dfs(1) # 매개변수 1



