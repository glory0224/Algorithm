# 한번만 등장한 문자

# def solution(s):
#     answer = ''
#     compare = ''
#     duplicate = ''
#     alphabet = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0,
#                 'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
#                 'k':0, 'l':0, 'm':0, 'n':0, 'o':0,
#                 'p':0, 'q':0, 'r':0, 's':0, 't':0,
#                 'u':0, 'v':0, 'w':0, 'x':0, 'y':0,
#                 'z':0}
    
#     for i in s:
#         for key, value in alphabet.items():
#             if i == key and i not in compare:
#                 alphabet[key] += 1
#                 compare += i
#             elif alphabet[key] > 1:
#                 duplicate += i
#                 print(duplicate)
#             elif i not in duplicate:
#                 answer += i
                
#     return sorted(answer)

# 접근 시도를 딕셔너리를 통해 알파벳 하나하나 나열해서 비교하는 식으로 코드 구현을 했다. 
# 비효율적인 코드를 짰다.

def solution(s):
    answer = ''
    count = {} # 빈 딕셔너리를 생성
    for c in s:
        count[c] = count.get(c, 0) + 1 # 해당하는 알파벳의 개수 추가

    for c in sorted(count): # 정렬된 딕셔너리에서 키를 뽑는다. 
        if count[c] == 1:
            answer += c
        
    return answer

print(solution("aabbfaafsafdggaz"))
