# [1차] 비밀 지도 문제

# 이진수 변환 후, 문자열 처리

def solution(n, arr1, arr2):
    answer = []
    
    arr1_bin = []
    
    arr2_bin = []
    
    for val1, val2 in zip(arr1, arr2):
        # 길이가 짧으면 길이 차이만큼 0을 앞에 추가
        if len(bin(val1)[2:]) < n:
            zero = '0' * (n-len(bin(val1)[2:]))
            arr1_bin.append(zero + bin(val1)[2:])
        else:
            arr1_bin.append(bin(val1)[2:])

        if len(bin(val2)[2:]) < n:
            zero = '0' * (n-len(bin(val2)[2:]))
            arr2_bin.append(zero + str(bin(val2)[2:]))
        else:
            arr2_bin.append(bin(val2)[2:])
    
    print(arr1_bin)
    print(arr2_bin)
    
    for bin1, bin2 in zip(arr1_bin, arr2_bin):
        tmp = ''
        # 조건에 맞게 벽과 아닌 경우 분기해서 문자열 채움
        for char1, char2 in zip(bin1, bin2):
            if char1 == '1' or char2 == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
        
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) # ["######", "###  #", "##  ##", " #### ", " #####", "### # "]

