# 자연수 뒤집어 배열로 만들기

def solution(n):
    
    n_str = str(n)
    
    n_str_list = list(map(int, n_str))
    
    return n_str_list[::-1]

print(solution(12345)) # [5, 4, 3, 2, 1]