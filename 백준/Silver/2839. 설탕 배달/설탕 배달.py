def solution(N):
    answer = 9999
    if N % 5 == 0:
        answer = min(answer, N // 5)
    if N % 3 == 0:
        answer = min (answer, N // 3)
    if (N % 5) % 3 == 0:
        s = N // 5
        s += (N%5)//3
        answer = min(answer, s)
    elif (N % 3) % 5 == 0:
        s = N // 3
        s += (N%3) // 5
        answer = min(answer, s)
    five = 5
    three = 3
    s = 0
    absolute = N
    while True:
        if (N - five) < 0:
            break
        N = N - five
        s += 1
        if N % three == 0:
            tmp = N // three
            answer = min(answer, s + tmp)
    if answer == 9999:
        answer = -1
    return answer
        

if __name__ == "__main__":
    N = input()
    ret = solution(int(N))
    print(ret)