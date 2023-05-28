
def solution(s, skip, index):
    # 알파벳 문자열 입력받기
    answer = 'abcdefghijklmnopqrstuvwxyz'

    result = []

    for i in skip:
        if i in answer:
            answer = answer.replace(i, "")
    
    # 문자들을 돌면서 그 문자들 위치에 인덱스 값을 더해서 이동한 문자 추출
    # 문자 위치가 z위치를 넘어가면 다시 a부터 시작하도록
    for j in s:
        result.append(answer[(answer.index(j) + index) % len(answer)])


    return "".join(result)

