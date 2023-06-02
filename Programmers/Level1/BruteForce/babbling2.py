# 옹알이 2 문제

# 접근 코드

# 딕셔너리 구조를 활용해서 카운트 해주는 방식으로 문제 접근 (실패)

# def solution(babbling):
#     answer = 0
    
#     possible = {"aya" : 0, "ye":0, "woo": 0, "ma" : 0}
    
#     for babble in babbling:
#         if babble in ["aya", "ye", "woo", "ma"]:
#             answer += 1
#         else:
#             for key in possible.keys():
#                 if key in babble:
#                     possible[key] += 1
            
#     for cnt in possible.values():
#             if cnt < 2:
#                 answer += 1
            
#     return answer



# 다른 접근 (while문 사용)

def pronounce(word):
    last = 0 # 같은 발음을 방지하지 위한 flag 변수
    while word:
            
        # 발음 할 수 있는 단어이고, 연속되지 않은 경우
        if word[:3] == 'aya' and last != 1: 
            word = word[3:]
            last = 1
        elif word[:2] == 'ye' and last != 2:
            word = word[2:]
            last = 2
        elif word[:3] == 'woo' and last != 3:
            word = word[3:]
            last = 3
        elif word[:2] == 'ma' and last != 4:
            word = word[2:]
            last = 4
        else:
            # 단어가 어디에서도 잘리지 않은 경우
            break
    
    return word
    

def solution(babbling):
    
    answer = 0
    
    # 향상 for문으로 발음할 문자 가져오기
    for word in babbling:
        # for문으로 나온 word는 참조만 할 수 있지 수정을 할 수 없었다.
        # 그래서 함수의 매개변수로 word를 넣고 나온 word의 값을 재할당해서 로직 수정
        word = pronounce(word) 

        if not word:
            answer += 1
    
    return answer
        
    

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
