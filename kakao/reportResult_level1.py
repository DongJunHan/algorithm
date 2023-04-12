def solution(id_list:list, report:list, k:int):
    """
        * 신고자가 중복으로 같은 사람을 신고한건 한 건으로 처리해야함.
        * 결과를 신고자가 몇 개를 각각 받는지를 알아야한다. 그래서 신고당한자 count를 K번 이상신고된 사람 처리한 다음에 어떤식으로 할건지
    """
    
    length = len(id_list)
    report_list = {}
    id_lists = {}
    lists = {}
    answer = {}
    # 신고자가 같은 신고 중복으로 하는 부분 막아주는 로직.
    for i in range(length):
        id_lists[id_list[i]] = 0
        answer[id_list[i]] = 0
    
    # 해시맵에서 key는 중복으로 삽입이 불가능 한 것에서 착안.
    # list(set(report)) => set함수를 통하여 중복제거가 가능하다.
    for r in report:
        report_list[r] = 0
    
    for i in range(length):
        temp = id_lists.copy()
        temp.pop(id_list[i])
        lists[id_list[i]] = temp
    #신고자 신고당한자 매칭
    for key in report_list.keys():
        arr = key.split()
        id_lists[arr[1]] += 1
        lists[arr[0]][arr[1]] = 1
    #K번의 신고 횟수가 넘어가는거 찾아서 메일링할 대상에 카운트
    for key in id_lists.keys():
        if id_lists[key] >= k:
            for key1 in lists.keys():
                if key1 is key:
                    continue
                if lists[key1][key] == 1:
                    answer[key1] += 1
    
    a = []
    for j in answer.keys():
        for i in id_list:
            if j == i:
                a.append(answer[j])
    return a


if __name__ == "__main__":
    # id_list = ["muzi", "frodo", "apeach", "neo"]
    id_list = ["con", "ryan"]
    # report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 2
    print(solution(id_list, report, k))


#답.
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer
