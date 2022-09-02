#11054번 백준 가장 긴 바이토닉 부분 수열 

import sys

T = int(input())

A = list(map(int, sys.stdin.readline().split()))

long_dp = [1 for i in range(T)]

short_dp = long_dp[:]

sub_len = [0] * T


# 증가하는 수열의 길이를 구하기 위한 dp for문 
for i in range(T):
    for j in range(i):
        if A[i] > A[j]:
             long_dp[i] = max(long_dp[i], long_dp[j] + 1)  


# 감소하는 수열의 길이를 구하기 위한 역정렬         
A.reverse()

# A reverse 하고 가장 긴 길이를 구해주면 역정렬된 가장 긴 감소하는 길이 dp가 만들어진다.
for i in range(T):
    for j in range(i):
        if A[i] > A[j]:
            short_dp[i] = max(short_dp[i], short_dp[j] + 1)

# 구한 후에 다시 reverse를 적용하면 반대로 뒤에서부터 감소하는 (뒤에서부터 증가하는) 가장 긴 배열이 된다. 
short_dp.reverse()

print(long_dp)
print(short_dp)

# 두개 인덱스끼리 더하면서 긴 증가와 긴 감소에 해당하는 경우의 수를 다 더한다. 
for i in range(T):
    sub_len[i] =  long_dp[i] + short_dp[i]

# 그 중에서 가장 긴 길이의 바이토닉 수를 출력한다.( 이때 -1을 하는 이유는 i 속한 기준이 되는 숫자가 중복되는 것을 방지하기 위해서)
# ex) 주어진 수열의 바이토닉 수열은 1,2,3,4,5,2,1 형태이며 이때 기준이 되는 값은 5이다.
# -> 증가하는 수열 = [1, 2, 3, 4, 5] , 감소하는 수열 = [5, 2, 1] 이고 이때 중복되는 5의 값이 두번 계산되니까 -1 해준다. 
print(max(sub_len)-1)    


# 정리하기 

# for i in range(T):
#     for j in range(i):
#         if A[i] > A[j]:
#              long_dp[i] = max(long_dp[i], long_dp[j] + 1)  

# 위의 이중 for문에 대한 결과는 
#  A = [ 1 5 2 1 4 3 4 5 2 1 ] 
#  long_dp = [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]

# 헷갈려서 적어보는 동작 원리 

# ex) long_dp[2] = 2가 어떻게 나왔는가
# 기본적으로 long_dp 에는 1의 값이 들어가 있다.
# A[1] > A[0] = 5 > 1 조건에 만족한다. long_dp[1] = 1, long_dp[0] + 1 = 2 값이 들어 가고 max(1, 2) -> long_dp[1] = 2 값이 최종적으로 들어간다.  j는 0이고 i 는 1 이기 때문에 j 를 더 돌리지 않고 종료   
# A[2] > A[0] = 2 > 1 조건에 만족한다. long_dp[2] = 1, long_dp[0] + 1 = 2 값이 들어가고 똑같이 더 큰 2 값을 long_dp[2]에 저장, i가 2이기 때문에 j는 0~1까지 총 두 번 돌아야 한다. 
# A[2] > A[1] = 2 > 5 조건에 만족하지 않는다. 따라서 if문을 실행하지 않고 넘어간다. -> 최종 값 2 안에 j가 들어있는 if문 종료 


# 이런 식으로 T까지 반복하면서 값을 구해주면 long_dp = [1, 2, 2, 1, 3, 3, 4, 5, 2, 1] 값이 나온다. 

# 주의할 점은 이중 for문의 j는 항상 0부터 i-1 까지 돌린다는 것!!


