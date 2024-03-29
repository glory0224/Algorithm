# 직사각형 넓이

# 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
# 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 
# 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# dots의 길이 = 4
# dots의 원소의 길이 = 2
# -256 < dots[i]의 원소 < 256
# 잘못된 입력은 주어지지 않습니다.

# dots	
# [[1, 1], [2, 1], [2, 2], [1, 2]]
# [[-1, -1], [1, 1], [1, -1], [-1, 1]]
# result
# 1
# 4

def solution(dots):
    # x축(가로) 리스트 받기
    x_list = [dots[i][0] for i in range(len(dots))]
    # y축(세로) 리스트 받기
    y_list = [dots[i][1] for i in range(len(dots))]

    width = max(x_list) - min(x_list)
    height = max(y_list) - min(y_list)

    answer = width * height

    return answer

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))