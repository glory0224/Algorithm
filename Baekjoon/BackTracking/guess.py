# 백준 1248번 맞춰봐 문제 

# https://velog.io/@jaenny/%EB%B0%B1%EC%A4%80-1248-%EB%A7%9E%EC%B6%B0%EB%B4%90-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython

def check(index) :
  s = 0
  for i in range(index, -1, -1) :
    s += ans[i]
    if sign[i][index] == 0 :
      if s != 0 :
        return False
    elif sign[i][index] < 0 :
      if s >= 0 :
        return False
    elif sign[i][index] > 0 :
      if s <= 0 : 
        return False
  return True

def go(index) :
  if index == n :
    return True
  
  if sign[index][index] == 0 :
    ans[index] = 0
    return check(index) and go(index+1)
  else :
    for i in range(1, 11) :
      ans[index] = i * sign[index][index]
      if check(index) and go(index+1) : return True 
    return False

n = int(input())
s = input()

sign = [[0]*n for _ in range(n)]
ans = [0]*n # 정답 숫자들
cnt = 0

# sign 배열 채우기
for i in range(n) :
  for j in range(i,n) :
    if s[cnt] == '0' :
      sign[i][j] = 0
    elif s[cnt] == '+' :
      sign[i][j] = 1
    else :
      sign[i][j] = -1
    cnt += 1

#print(sign)
go(0)
print(' '.join(map(str, ans)))
