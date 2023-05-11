# 정곤이의 단조 증가하는 수

# 정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

# 그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

# 어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

# 예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

# 양의 정수 N 개 A1, …, AN이 주어진다.

#  1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.

# 두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.


# [출력]

# 각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.

# 만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

# 입력
# 1
# 4
# 2 4 7 10

# 출력
# #1 28

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    A = list(map(int, input().split()))

    # 최대값 변수 -1로 초기화 (없을 경우 -1 출력)
    max_value = -1
    
    
    # 이중 for문 돌면서 최대값 결과 만들기
    for i in range(N):
        for j in range(i+1, N):
            # A[i] * A[j] 
            prod = A[i] * A[j]
            # prod 변수를 str로 변환
            str_prod = str(prod)
            
            # 단조 증가하는 수가 맞는지 flag 변수 선언
            is_increasing = True
        
           # str_prod의 길이만큼 반복문 돌면서 단조 증가하는 수가 아닌 경우 탐색
            for k in range(1, len(str_prod)):

                if str_prod[k] < str_prod[k-1]: # 지금의 예시는 1의 자리수 값이 10의 자리수 값보다 작으면 단조 증가하는 수가 아님
                    # flag 변수 변경
                    is_increasing = False
                    break # 종료
                
            # 최대값 갱신
            if is_increasing and prod > max_value:
                max_value = prod    
    
    print(f"#{tc} {max_value}")
                

