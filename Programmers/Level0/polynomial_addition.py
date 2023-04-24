# 다항식 더하기 문제

# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 

# 같은 식이라면 가장 짧은 수식을 return 합니다.
# (예를 들어 "3x + 7 + x"와 "4x + 7"은 동일한 다항식을 나타내지만, "4x + 7"은 변수의 항을 1개만 포함하므로, "4x + 7"이 가장 짧은 수식입니다.)


# 제한사항

# 0 < polynomial에 있는 수 < 100

# polynomial에 변수는 'x'만 존재합니다.

# polynomial은 0부터 9까지의 정수, 공백, ‘x’, ‘+'로 이루어져 있습니다.

# 항과 연산기호 사이에는 항상 공백이 존재합니다.

# 공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.

# 하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.

# " + 3xx + + x7 + "와 같은 잘못된 입력은 주어지지 않습니다.

# "012x + 001"처럼 0을 제외하고는 0으로 시작하는 수는 없습니다.

# 문자와 숫자 사이의 곱하기는 생략합니다.

# polynomial에는 일차 항과 상수항만 존재합니다.

# 계수 1은 생략합니다.

# 결괏값에 상수항은 마지막에 둡니다.

# 0 < polynomial의 길이 < 50

# 입출력 예
# polynomial	result
# "3x + 7 + x"	"4x + 7"
# "x + x + x"	"3x"


def solution(polynomial):
    # 다항식을 항으로 분리하여 리스트로 저장
    terms = polynomial.split(" + ")

    # 계수를 저장할 딕셔너리 생성
    coefficients = {}

    # 각 항을 하나씩 처리하여 계수를 딕셔너리에 저장
    for term in terms:
        # 만약에 항에 x가 없다면 상수항이므로 0번째 key에 저장
        if "x" not in term:
            coefficients[0] = coefficients.get(0, 0) + int(term)
        else:
            # x가 있는 경우 항에서 계수와 변수 부분을 분리
            coeff, var = term.split("x")
            coeff = coeff.strip() # 계수 부분의 공백 제거
            var = var.strip() # 변수 부분의 공백 제거

            # 계수가 없는 경우 1로 처리
            if coeff == "":
                coeff = "1"

            # 변수가 없는 경우 1로 처리
            if var == "":
                var = "1"
            
            # 계수와 변수를 int형으로 변환하여 딕셔너리에 저장
            coefficients[int(var)] = coefficients.get(int(var), 0) + int(coeff)

    # 결과값을 저장할 변수 초기화
    result = ""

    # 변수의 차수를 기준으로 내림차순 정렬하여 계수와 변수를 결합하고 결과값 생성
    for key in sorted(coefficients.keys(), reverse=True):
        # 상수항 계수일때 
        if key == 0:
            result += str(coefficients[key])
        
        # 일차항 계수 
        elif key == 1:
            if coefficients[key] == 1:
                result += "x"
            elif coefficients[key] == -1:
                result += "-x"
            else:
                result += f"{coefficients[key]}x"
        
        # 이차항 계수(현재 문제에서는 일차항과 상수항만 나온다고 제시 했기 때문에 고려하지 않아도 된다. 하지만 이차항의 계수까지 고려한다면 아래와 같이 코드를 작성한다.)
        # else:
        #     if coefficients[key] == 1:
        #         result += f"x^{key}"
        #     elif coefficients[key] == -1:
        #         result += f"-x^{key}"
        #     else:
        #         result += f"{coefficients[key]}x^{key}"
        
        # 각 항마다 "+" 기호를 붙여줌
        result += " + "

    
    # 결과값의 마지막 "+" 기호 제거 후 반환
    result = result.rstrip(" + ")
    return result if result else "0"

print(solution("3x + 7 + x"))
print(solution("x + x + x"))


        