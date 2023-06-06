# 신고 결과 받기

# 딕셔너리 활용해서 구현한 문제

# 시도
# def solution(id_list, reports, k):
#     answer = []
    
#     declare_cnt = {n:0 for n in id_list}
#     declare_group = {n:[] for n in id_list}
#     id_check = []
    
#     for report in reports:
#         id, declare_id = report.split()
#         declare_group[id].append(declare_id)
#         # 한 id가 같은 declare_id를 신고한 경우 횟수는 1회만 증가
#         if (id, declare_id) not in id_check:
#             declare_cnt[declare_id] += 1 # 신고횟수 증가
#             id_check.append((id, declare_id))
    
#     print(declare_cnt)
    
#     return answer

def solution(id_list, reports, k):
    # 중복 없이 각 신고 당한 id 그룹을 담을 딕셔너리
    report_group = {ID:set() for ID in id_list}

    # reports 에서 뽑은 report에서 신고한 id, 신고당한 id 분리
    for report in reports:
        u, r = report.split()
        report_group[r].add(u) # report에 id를 신고한 id를 담는다.
    
    # 신고를 성공한 횟수 카운트 딕셔너리
    success = {ID:0 for ID in id_list}

    # 순서대로 id에 메일을 보내기 때문에 id_list에서 바로 id를 뽑는다.
    for id in id_list:
        # k 이상만 유효
        if k <= len(report_group[id]):
            for reporter in report_group[id]: # 신고한 그룹의 신고자를 뽑아서 
                success[reporter] += 1 # 그 신고자에게 보낼 메일 cnt 증가
    
    # print(report_group)

    # print(success)

    answer = list(success.values()) # list 변환

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) # result [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) # result [0,0]