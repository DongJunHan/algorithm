def solution(n):
    answer = 0
    return len([i for i in range(1,n+1,2) if n % i == 0])
