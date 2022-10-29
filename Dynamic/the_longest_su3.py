# 백준 12738번 가장 긴 증가하는 부분 수열 3
# https://claude-u.tistory.com/442


# 나무위키 LIS(Longest Increasing Subsequence) 설명 - https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2

# https://folivora.tistory.com/83 - bisect_left 설명 

"""
아이디어 

if: 현재 값이 수열에서 가장 크다면

--> dp의 가장 뒤에 값을 추가

else: 아니라면

--> 자신보다 큰 수 중 최솟값과 대치(이진탐색 이용)

이런식으로 진행하면 시간복잡도 O(nlogn)에 가장 긴 dp의 길이를 알아낼 수 있다.

-- 반례 --

그러나 만약 다음과 같은 수열이 주어지면

A = 3 5 7 9 2 1 4 8

우리가 예상하는 dp는 3 5 7 9 이지만

실제 dp는 1 4 7 8로 나온다.

따라서 해당 알고리즘은 정답 수열을 도출해내는 데에는 사용할 수 없다. = 길이만 도출 가능하고 각각의 수열을 출력하는 것에는 적합하지 않다.

"""


from bisect import  bisect_left # 이진 탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다. 

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    print(" i : " + str(i))
    k = bisect_left(dp, i) # 자신이 들어갈 위치 k 
    print("k : " + str(k))
    print("len(dp) : " + str(len(dp)))
    if len(dp) <= k: # i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i # 자신보다 큰 수 중 최솟값과 대체 
    
print(len(dp))
