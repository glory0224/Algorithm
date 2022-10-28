# 백준 2109번 순회강연 
# https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-2109-%EC%88%9C%ED%9A%8C%EA%B0%95%EC%97%B0
import heapq

n=int(input())
lst=[]
for i in range(n):
  lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1]))
p_list=[]
for i in lst:
  heapq.heappush(p_list, i[0])
  if (len(p_list)>i[1]):
    heapq.heappop(p_list)

print(sum(p_list))