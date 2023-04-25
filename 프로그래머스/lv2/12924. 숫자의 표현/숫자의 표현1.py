def solution(n):
    answer = 0
    i = 1
    while True:
        sum_n = 0
        for j in range(i,n+1):
            sum_n += j
            print(f"j:{j}")
            if sum_n == n:
                print("\n")
                answer += 1
                break
            if sum_n > n:
                break
        if i == n:
            break
        else:
            i += 1
    return answer


if __name__ == "__main__":
    n = 100
    ret = solution(n)
    print(f"ret={ret}")