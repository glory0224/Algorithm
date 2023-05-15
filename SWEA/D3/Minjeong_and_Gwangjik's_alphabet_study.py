# 민정이와 광식이의 알파벳 공부

# 비트 마스킹 풀이 방식 사용 (비트 마스크 모르면 난이도 어렵다..)

# 아기 광직이는 열심히 받아쓰기를 했지만, 아직 알파벳을 다 떼지 못했다.

# 아기 민정이는 그런 광직이가 반 친구들에게 놀림 받지 않을까 걱정이 되어 직접 학습지를 만들어 광직이에게 알파벳을 가르쳐 주려고 한다.

# (아기 민정이는 광직이보다 동생이지만, 알파벳을 잘 알고 있다.)

# 민정이는 광직이가 따라 적을 수 있도록 알파벳 연습용 단어 세트를 여러 개 만들 것이다.

# 광직이는 현재 N개의 영어 단어를 알고 있고, 이 중 몇 개를 골라 하나의 세트로 만드는데, 각 세트 안에 포함된 단어의 순서는 중요하지 않다.

# 광직이가 모든 알파벳을 골고루 공부할 수 있도록, 단어 세트에는 26개의 알파벳 소문자가 모두 포함되어 있어야 한다.

# 즉, 모든 알파벳 소문자에 대해, 단어 세트 안에 그 문자를 포함하는 단어가 적어도 하나 존재해야 한다.

# 단어 세트가 많이 있을수록 광직이가 알파벳을 더 잘 외울 것이라 생각한 민정이는 서로 다른 세트를 최대한 많이 만들어 주려고 한다.

# 아기 민정이가 광직이를 위해 몇 개의 단어 세트를 만들 수 있을지 구해주자!

# [입력]

# 첫 번째 줄에 테스트 케이스의 수 TC 가 주어진다.

# 이후 TC 개의 테스트 케이스가 새 줄로 구분되어 주어진다.

# 각 테스트 케이스는 다음과 같이 구성되어 있다.

# > 첫 번째 줄에 아기 민정이가 아는 단어의 개수 N이 주어진다. (1 <= N <= 15) 

# > 이후 N개의 줄에 민정이가 아는 단어들이 한 줄에 하나씩 주어진다.

# > 각 단어는 공백 없이 알파벳 소문자로만 이루어져 있다.

# > 단어 하나의 길이는 1이상 100이하 이며, 모든 단어는 서로 다르다.

# [출력]

# 각 테스트 케이스마다 ‘#t’(t 는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

# 민정이가 만들 수 있는 서로 다른 단어 세트의 개수를 출력한다.

# 입력
# 2       # 테스트 케이스의 수 TC = 2
# 10
# cozy
# lummox
# gives
# smart
# squid
# who
# asks
# for
# job
# pen
# 6
# abcdefghi
# jklmnopqr
# stuvwxyz
# zyxwvuts
# rqponmlkj
# ihgfedcba

# 출력
# #1 1
# #2 27

def find_word_set(words):

    n = len(words)
    words_bit = [0] * n


    for i, word in enumerate(words):
        for c in word:
            # 해당 알파벳의 비트를 구해서 words_bit와 or 연산을 길이만큼 진행 
            words_bit[i] |= (1 << ord(c) - ord('a'))
        
    ans = 0 # 정답 초기화

    for i in range(1, 1 << n):
        # 모든 알파벳이 포함되어 있는지 확인용 변수
        included = 0

        for j in range(n):
            if i & (1 << j):
                included |= words_bit[j] # or 연산으로 최대한 1이 많게끔 

        # 알파벳 26개의 비트가 전부 1인지 확인
        if included == (1 << 26) - 1:
            ans += 1
    
    return ans
        


T = int(input())

for tc in range(1, T+1):
    # 단어 개수
    N = int(input())

    # 단어들
    words = [input().strip() for _ in range(N)]

    answer = find_word_set(words)

    print(f"#{tc} {answer}")

