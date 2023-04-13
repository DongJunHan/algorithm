#https://school.programmers.co.kr/learn/courses/30/lessons/92334/
def solution(id_list, report, k):
    answer = []
    check = {}
    for i in id_list:
        check[i] = {}
        for j in id_list:
            check[i][j] = 0
    
    receive = {i:0 for i in id_list}
    for i in report:
        name_arr = i.split(" ")
        if check[name_arr[0]][name_arr[1]] == 1:
            continue
        check[name_arr[0]][name_arr[1]]  = 1

    for i in id_list:
        ret = 0
        for j in id_list:
            if check[j][i] == 1:
                ret += 1
        if ret >= k:
            for j in id_list:
                if check[j][i] == 1:
                    receive[j] += 1

    
    for i in id_list:
        answer.append(receive[i])

    return answer

if __name__ == "__main__":
    # id_list = ["muzi", "frodo", "apeach", "neo"]
    id_list = ["con", "ryan"]
    # report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    # k = 2
    k = 3
    ret = solution(id_list, report, k)
    print(f"ret={ret}")