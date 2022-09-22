# 백준 15661번 링크와 스타트 

# https://intrepidgeeks.com/tutorial/baekjun-15661-links-and-starts-pythonpython

# DFS(백트래킹)

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def go(index, start, link) :
  if index == n :
    if len(start) == n or len(link) == n :
      return -1
    
    team_start = 0
    team_link = 0

    for i in range(len(start)) :
      for j in range(i+1, len(start)) :
        # 인덱스가 서로 같은 경우는 0에 해당하기 때문에 패스한다.
        if i == j : continue
        team_start = team_start + s[start[i]][start[j]] + s[start[j]][start[i]]
    
    for i in range(len(link)) :
      for j in range(i+1, len(link)) :
        if i == j : continue
        team_link = team_link + s[link[i]][link[j]] + s[link[j]][link[i]]

    diff = abs(team_start - team_link)
    return diff
  
  if len(start) > n or len(link) > n : return -1

  ans = -1

	# index의 사람을 start 팀에 넣었을 때
  team_start = go(index+1, start+[index], link)
  if ans == -1 or (team_start != -1 and ans > team_start) :
    ans = team_start
  
	# index의 사람을 link 팀에 넣었을 때
  team_link = go(index+1, start, link+[index])
  if ans == -1 or (team_link != -1 and ans > team_link) :
    ans = team_link

  return ans

print(go(0,[],[]))

# 또 다른 풀이 

n = int(input())
stats = [list(map(int, input().split())) for i in range(n)]
visited = [0] * n
ans = 99999

def is_it():
    global ans
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += stats[i][j]
            elif not visited[i] and not visited[j]:
                link += stats[i][j]
    ans = min(ans, abs(start - link))
    return

def resolve(iter):
    if iter == n:
        is_it()
        return
    visited[iter] = 1
    resolve(iter + 1)
    visited[iter] = 0
    resolve(iter + 1)
resolve(0)

print(ans)
