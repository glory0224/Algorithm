# 해시 문제

def solution(phone_book):

    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # 맨 앞에 접두어 길이만큼만 비교한다.
            return False
        
    return answer


print(solution(["123","456","789"]))
