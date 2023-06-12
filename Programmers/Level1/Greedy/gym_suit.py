# 체육복 문제

def solution(n, lost, reserve):

    # 여벌 체육복이 있는 학생이 체육복을 도난
    # 도난 당한 학생은 중복이 없다. (set)
    # 여벌 체육복이 있는 학생도 중복 없다. (set)

    # 도난 당한 학생
    real_lost = set(lost) - set(reserve)

    # 빌려줄 수 있는 학생
    real_reserve = set(reserve) - set(lost)

    # 전체 인원에서 잃어버린 학생 수를 빼고 현재 들을 수 있는 학생 수를 더한다.
    cnt = n - len(real_lost)

    # 여벌이 있는 학생 번호 앞 번호나 뒤 번호에서 빌려주는 경우를 세준다.
    for i in real_reserve:
        if i - 1 in real_lost: # 여벌 학생 앞번호가 잃어버린 학생인 경우
            cnt += 1
            real_lost.remove(i-1)

        elif i + 1 in real_lost: # 여벌 학생 뒷번호가 잃어버린 학생인 경우
            cnt += 1
            real_lost.remove(i+1)
    
    return cnt


print(solution(5, [2, 4], [1,3,5])) # result 5
print(solution(5, [2, 4], [3])) # result 4
print(solution(3, [3], [1])) # result 3
