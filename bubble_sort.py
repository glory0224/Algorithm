# 백준 1517번 버블 소트 

# 문제는 버블 소트이지만 병합 정렬를 이용해서 풀어야 하는 문제 
# https://jokerldg.github.io/algorithm/2021/09/12/bubble-sort.html


import sys

# 표현식을 간단하게 쓰고자 lamda 사용 
input = lambda: sys.stdin.readline().rstrip()
N = int(input())

A = list(map(int, input().split()))

ans = 0

def merge_sort(start, end):
    global ans, A
    
    
    
    if start < end:
        mid = (start+end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        a = start
        b = mid+1
        temp = []

        while a <= mid and b <= end:
            if A[a] <= A[b]:
                temp.append(A[a])
                a += 1
            else:
                temp.append(A[b])
                b += 1
                ans += (mid - a + 1)
    
        if a <= mid:
            temp = temp + A[a:mid + 1]
        if b <= end:
            temp = temp + A[b:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]

merge_sort(0, N - 1)
print(ans)

