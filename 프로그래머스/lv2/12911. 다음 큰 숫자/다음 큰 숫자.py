def solution(n):
    answer = 0
    c = get_binary(n)
    for i in range(n+1, 1000000):
        check = check_one_cnt(i, c)
        if check:
            answer = i
            break
    return answer

def check_one_cnt(n, cnt):
    oc = 0
    answer = True
    while n > 0:
        remain = n % 2
        if remain == 1:
            oc += 1
        if oc > cnt:
            answer = False
            break
        n = n // 2
    if oc < cnt:
        answer = False
    return answer

def get_binary(n):
    cnt = 0
    while n > 0:
        remain = n % 2
        n = n // 2
        if remain == 1:
            cnt += 1
    return cnt
        
        
        
    