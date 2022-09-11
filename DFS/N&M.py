# 백준 15649번 N과 M문제 
# 재귀함수를 잘 이용한 문제
# 브루트포스 백트레킹 기법 활용 문제 


n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop() # 재귀함수가 종료될 때마다 pop 실행, 중복된 수를 빼내기 위한 코드 
 
dfs()
 
