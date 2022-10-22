# 백준 11399번 파이썬 

n = int(input())

# 기다리는 사람들 리스트 형태로 입력 받는다.
peoples = list(map(int, input().split()))

peoples.sort() # 인출 시간이 작은 순서대로 정렬 

# 정답 변수 
answer = 0

for x in range(1, n+1):
    # 리스트의 0번째 수부터 x번째 수까지를 더해줍니다.
    answer += sum(peoples[0: x])
    

print(answer) 