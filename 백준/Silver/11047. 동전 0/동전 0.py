import sys
def solution(K, arr):
    answer = 0
    for i in range(len(arr)-1, -1, -1):
        if K // arr[i] > 0:
            answer += K // arr[i]
            K = K % arr[i]
    return answer

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for i in range(N):
        a = input()
        arr.append(int(a))
    print(solution(K, arr))