# 백준 2109번 순회강연 
# https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-2109-%EC%88%9C%ED%9A%8C%EA%B0%95%EC%97%B0

"""
 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다. 
 각 대학별로 d 기한 안에 와서 강연을 해주면 돈을 받는다.
 기한이 같은 대학 중 최대로 돈을 벌 수 있는 경우의 수를 더해주면 된다. 
"""

import heapq

# 갈 수 있는 대학 수 입력 
n=int(input())

lst=[]
for i in range(n):
  lst.append(list(map(int, input().split())))

# 일자별로 오름차순해서 일정을 순차적으로 갈 때 어느 대학이 제일 돈을 많이주는지 비교한다. 
# 따라서 lst배열의 1번 인덱스를 기준으로 오름차순 정렬 
lst.sort(key=lambda x: (x[1]))

p_list=[]
for i in lst:
  heapq.heappush(p_list, i[0])
  print("p_list : " + str(p_list))
  print("i[1] : " + str(i[1]))
  if (len(p_list)>i[1]): # 마감일을 넘기는 경우는 heapq.heappop 메서드를 통해 가장 작은 값을 빼준다. 
    heapq.heappop(p_list)

print(sum(p_list))
