from math import ceil, sqrt
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]
# n이 소수인지 판정
def isprime(n:int):
    """
        에라토스테네스의체로 구하게 되면 자릿수가 커질시 무조건 시간초과가 발생하게 된다.
        그렇기 때문에 아래와 같은 방법으로 소수를 판별해야 한다.
    """
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n:int, k:int):
    a = n
    r = conv(n, k)
    print(r)
    arr = []
    answer = 0
    if k < 10:
        while True:
            if (k * k) > a:
                arr.append(a % k)
                arr.append(a // k)
                break
            else:
                arr.append(a % k)
            a = a // k
        s = ""
        length = len(arr)
        for i in range(length):
            s += str(arr.pop())
        n = int(s)

    length = len(str(n))
    arr = str(n).split('0')
    for num in arr:
        if len(num) == 0:
            continue
        if isprime(int(num)):
            answer += 1
    return answer

if __name__ == "__main__":
    # n = 437674
    # n = 110011
    n = 1000000
    k = 3
    # k = 10
    print(solution(n, k))