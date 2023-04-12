def self_loop(k,n,tabulation):
    if k == 0:
        return n
    if n == 1:
        return 1

    key = str(k) +","+ str(n)
    if key in tabulation.keys():
        return tabulation[key]
    sum_ =  self_loop(k-1, n, tabulation) + self_loop(k, n-1, tabulation)
    tabulation[key] = sum_
    return sum_
def solution():
    test_case = input()
    answer = []
    for i in range(int(test_case)):
        print("input k: ")
        k = input()
        print("input n: ")
        n = input()
        tabulation = {}
        answer.append(self_loop(int(k), int(n), tabulation))
    return answer
if __name__ == "__main__":
    answer = solution()
    for i in answer:
        print(i)