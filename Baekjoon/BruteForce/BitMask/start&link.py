# 백준 14889번 비트마스크를 이용한 문제 풀이 


from sys import*
input = stdin.readline
# 팀이 결성되었을 경우 각 팀의 능력치를 모두 합하고 차이가 최소가 되는 값을 출력하는 함수 
def cal():
   teamA, teamB = 0, 0
   for i in range(n):
       for j in range(i+1, n):
           if player[i] and player[j]:
               teamA += a[i][j] + a[j][i]
           if not(player[i] or player[j]):
               teamB += a[i][j] + a[j][i]
   return abs(teamA - teamB)
def solve(pos, cnt):
   res = INF
    #cnt가 반절(n/2)을 넘어가면 팀설정이 잘못되었다. 끝내버린다.
   if cnt > n//2: return res
   # pos가 마지막(n) 까지 탐색을 완료하였고, cnt가 반절(n/2)을 선택했으면 둘 씩 짝지어서 A팀, B팀 각각 계산을 해준다.
   if pos == n:
       if cnt == n//2: return cal()
       return res
   # 방식은 back_tracking과 유사하지만 비트마스킹은 1과 0으로 팀을 나눈다.
   player[pos]=1
   res = min(res, solve(pos+1, cnt+1))
    #print("result : " + str(res))
    #print("pos : " + str(pos))
    #print("cnt : " + str(cnt))
    #print("player : " + str(player[pos]))
   player[pos]=0
   res = min(res, solve(pos+1, cnt))
    #print("result : " + str(res))
    #print("pos : " + str(pos))
    #print("cnt : " + str(cnt))
    #print("player : " + str(player[pos]))
   return res
INF=1e9
n=int(input())
a=[]; SUM=0
player=[0]*n
a=[list(map(int,input().split())) for _ in range(n)]
print(solve(0, 0))
