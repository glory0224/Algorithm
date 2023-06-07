# 부족한 금액 계산

def solution(price, money, count):
    total = price
    for i in range(2, count+1):
        total += price * i
        
    # 단, 금액이 부족하지 않으면 0을 return 하세요.
    if total <= money:
        answer = 0
    else:
        answer = total - money

    return answer

print(solution(3, 20, 4)) # result 10