# 공던지기 문제

# https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%B5-%EB%8D%98%EC%A7%80%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
# 참고  

# def solution(numbers, k):
#     answer = 0
#     if len(numbers) < k * 2:
#         numbers = numbers * ((k*2) // len(numbers) + 1)
#     answer = numbers[2*(k-1)]
#     return answer

def solution(numbers, k):
    answer = numbers[2*(k-1) % len(numbers)]
    return answer