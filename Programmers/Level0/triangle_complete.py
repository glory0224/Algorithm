# 삼각형 완성조건

#https://school.programmers.co.kr/learn/courses/30/lessons/120889


def solution(sides):
    # 세변의 길이 0 체크
    if any(side <= 0 for side in sides):
        return 2
    
    max_side = max(sides)
    other_sides_sum = sum(sides) - max_side

    if max_side < other_sides_sum:
        return 1
    else:
        return 2

print(solution([1,2,3]))

# 다른 풀이

def solution2(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

print(solution2([1,2,3]))