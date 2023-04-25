def solution(n):
    answer = 0
    cache = [0 for i in range(n + 1)]
    cache[0] = 0
    cache[1] = 1
    cache[2] = 1
    for i in range(3, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n] % 1234567

def fibo(n, cache):
    if cache[n] != 0:
        return cache[n]
    if n == 2 or n == 1:
        cache[n] = 1
        return cache[n]
    if n == 0:
        cache[n] = 0
        return cache[n]
    cache[n] = fibo(n-1, cache) + fibo(n-2, cache)
    return cache[n]
    