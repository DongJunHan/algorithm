def solution(n):
    answer = 0
    i = 1
    while True:
        sum_n = 0
        for j in range(i,n+1):
            sum_n += j
            if sum_n == n:
                answer += 1
                break
            if sum_n > n:
                break
        
        if i == n:
            break
        else:
            i += 1
    return answer