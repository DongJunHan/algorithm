def solution(N):
    answer = 0
    arr = N.split("-")
    sub = []
    for i in range(len(arr)):
        if "+" not in arr[i]:
            sub.append(int(arr[i]))
        else:
            sub.append(sum(list(map(int, arr[i].split("+")))))
    if len(sub) == 1:
        return sub[0]
    answer = sub[0]
    for i in range(1, len(sub)):
        answer -= sub[i]
    return answer


if __name__ == "__main__":
    N = input()
    print(solution(N))