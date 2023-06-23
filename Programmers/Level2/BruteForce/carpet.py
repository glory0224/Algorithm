# 카펫 문제

# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 예시

# 갈 갈 갈 갈
# 갈 노 노 갈
# 갈 갈 갈 갈

# 갈색 개수 : 10, 노란색 개수 : 2 , return [4, 3]

def solution(brown, yellow):

    # 갈색의 높이와 너비 = 노란색 높이 + 2, 노란색 너비 + 2
    # bh, bw = yh + 2, yw + 2
    # 카펫 전체 크기 = brown + yellow = bh * bw
    # yellow = yh * yw = (bh - 2) * (bw - 2)
    # brown = bh + bh + bw + bw - 4(중복)

    for bh in range(1, brown // 2 + 1): # 열의 길이는 절반을 못넘김 (세로)
        # bw 식 도출 과정 (가로)
        # brown = bh + bh + bw + bw - 4
        # brown = 2bh + 2bw - 4
        # -2bw = -brown + 2bh - 4
        # 2bw = brown - 2bh + 4
        # bw = (brown - 2bh + 4) // 2
        bw = (brown - 2 * bh + 4) // 2 

        # yh와 yw 계산
        yh, yw = bh - 2, bw - 2

        # 만약 yh 와 yw 를 곱한 값이 yellow와 같고 (노란색 격자 크기)
        # brown + yellow 가 bh * bw와 같으면 (총 크기)
        # 카펫 가로와 세로 크기 반환
        if yh * yw == yellow and brown + yellow == bh * bw:
            return [bw, bh]

print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]
