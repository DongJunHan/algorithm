#https://school.programmers.co.kr/learn/courses/30/lessons/150370#qna
def solution(today, terms, privacies):
    answer = []
    term_map = {}
    days = 28
    for term in terms:
        term = term.split(" ")
        month = int(term[1])
        today_c = today.split(".")
        today_c[0] = int(today_c[0]) * (days * 12)
        today_c[1] = int(today_c[1]) * days
        today_c[2] = int(today_c[2])
        
        term_map[term[0]] = sum(today_c) - (month * days)
    for j in range(len(privacies)):
        privacie = privacies[j].split(" ")
        arr = privacie[0].split(".")
        arr[0] = int(arr[0]) * (days * 12)
        arr[1] = int(arr[1]) * (days)
        arr[2] = int(arr[2])
        today_c = term_map[privacie[1]]
        if sum(arr) <= today_c:
            answer.append(j+1)
    return answer

if __name__ == "__main__":
    today = "2020.01.01"
    terms = ["Z 3", "D 5"]
    privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    # today = "2022.05.19"
    # terms = ["A 6", "B 12", "C 3"]
    # privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    ret = solution(today, terms, privacies)
    print(f"ret={ret}")