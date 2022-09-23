#2529번 백준 부등호 문제 

# https://jinu0418.tistory.com/114

# 큰수인지 작은수인지 체크 

# 시작 할때 0부터 커지는 순서대로 for문이 돌아가기 때문에 아래와 같은 로직이면
# 결국 처음에 문자열 찍힌 숫자가 제일 작은 수이고 모든 경우의 수를 다 구한 마지막 값이 제일 큰 수가 된다. 
def check(i, j, k):
    if k == '<':
        return i<j
    else:
        return i>j



def solve(idx, s):
    global max_ans, min_ans

    if(idx==T+1):
        
        if(len(min_ans)==0):
            #print(len(min_ans))
            min_ans = s
            print("min : ", min_ans)
        else:
            max_ans = s
            print("max : ", max_ans)
        return

    for i in range(10):
        # 방문 여부 false
        if(visited[i]==0):
  
            print(s)
            if(idx==0 or check(s[-1], str(i), enequal[idx-1])):
                
                visited[i] = True
                solve(idx+1, s+str(i))
                visited[i] = False
                print("index : " , idx)
                #print("visited 의" + str(i) + "번째 불리언은 ", visited[i])
                    

T = int(input())

enequal= list(map(str, input().split()))

# 새롭게 숫자가 추가 될 때마다 앞의 숫자와 비교해주기 위한 check 함수 
visited = [0] * 10
# 최대값
max_ans = ""
# 최소값
min_ans = ""

# 재귀 함수 생성 
solve(0, "")

print(max_ans)
print(min_ans)

