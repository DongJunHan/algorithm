#https://school.programmers.co.kr/learn/courses/30/lessons/92334/
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     check = {id: {} for id in id_list}
#     for key in check.keys():
#         for i in id_list:
#             check[key][i] = 0
#     #중복 제거
#     for i in set(report):
#         name_arr = i.split(" ")
#         check[name_arr[1]][name_arr[0]]  = 1
#     for key, v in check.items():
#         if sum(v.values()) >= k:
#             for i in range(len(id_list)):
#                 answer[i] += check[key][id_list[i]]

#     return answer
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id:[] for id in id_list}

    for i in set(report):
        i = i.split(" ")
        dic_report[i[1]].append(i[0])
    print(dic_report)
    for key ,v in dic_report.items():
        if len(v) >= k:
            for j in v:
                answer[id_list.index(j)] += 1

    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    # id_list = ["con", "ryan"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"]
    # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 2
    # k = 3
    ret = solution(id_list, report, k)
    print(f"ret={ret}")