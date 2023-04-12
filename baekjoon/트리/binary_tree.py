def inord(n:int):
    global cnt
    if n <= N:
        inord(n*2)
        print(f"n: {n}, cnt: {cnt}")
        arr[n] = cnt
        cnt += 1
        inord(n*2 +1)



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0 for _ in range(N+1)]
    cnt = 1
    inord(1)
    print(f"#{test_case} {arr[1]} {arr[N//2]}\tarr:{arr}")