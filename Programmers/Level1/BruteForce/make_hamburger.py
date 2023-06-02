# 햄버거 만들기 문제

# 스택 자료구조 활용

def solution(ingredient):
    answer = 0
    stack = []
    make_order = [1,2,3,1]

    for ing in ingredient:
        stack.append(ing) # 스택에 값을 하나씩 넣어준다.
        if stack[-len(make_order):] == make_order: # LIFO - 맨 뒤에서부터 역순으로 읽었을 때 값이 동일한지 확인
            # stack = stack[:-4]는 해당 인덱스만큼 자른 뒤, 배열을 새로 할당해야하기 때문에 시간 초과가 발생한다.  
            del stack[-4:] # del은 있는 stack의 길이에서 뒤에 4개만 자르기 때문에 O(N) 만큼 소요
            # stack.pop() # pop() - 뒤에서 꺼내는 경우 O(1) 시간 복잡도 - 즉 O(N)만큼의 시간이 소요된다.
            # stack.pop()
            # stack.pop()
            # stack.pop() 
            answer += 1 # 햄버거 추가
            
    return answer

# 다른 풀이 방식

# def solution(ingredients):
#     answer = 0
#     stack = []

#     for ingredient in ingredients:
#         if ingredient == 1 and stack[-3:] == [1, 2, 3]:
#             # del stack[-3:]
#             stack.pop()
#             stack.pop()
#             stack.pop()

#             answer += 1
#         else:
#             stack.append(ingredient) 

#     return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))