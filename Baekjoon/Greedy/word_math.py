# 백준 1339번 단어 수학 
# https://yoonsang-it.tistory.com/41
# 브루트 포스 방식으로 푸는 것보다 그리디 알고리즘을 이용하여 풀어야 시간초과가 나지 않는다. 

import sys

n = int(sys.stdin.readline())

# 딕셔너리를 이용하여 알파벳 지정
alphabet_dict = {'A': 0, 'B': 0 , 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H' : 0, 'I':0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y':0, 'Z':0}

alphabet_list = []
answer = 0
pocket = []

for _ in range(n):
    alphabet = input()
    pocket.append(alphabet)
    #print(pocket)
    
for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet) - i -1) # 0번 인덱스부터 시작하기 때문에 
        #print(str(alphabet[i]) + str(alphabet_dict[alphabet[i]]))
        alphabet_dict[alphabet[i]] += num
        
for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)
        #print("alphabet_list : " + str(alphabet_list))
        
sorted_list = sorted(alphabet_list, reverse=True) # 내림차순 정렬
#print("sorted_list" + str(sorted_list) + "len : " + str(len(sorted_list)))

# A = 10000 * 9 = 90000
# C = 1010 * 8 = 8080
# G = 100 * 7 = 700
# D = 100 * 6 = 600
# E = 10 * 5 = 50
# B = 1 * 4 = 4
# F = 1 * 3 = 3

# 위와 같은 예시 방식으로 answer에 더해진다.
for i in range(len(sorted_list)):
    #print(str(sorted_list[i] * (9-i)))
    answer += sorted_list[i] * (9-i)
    
    
print(answer)
