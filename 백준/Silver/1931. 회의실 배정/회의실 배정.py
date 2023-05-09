import sys
def solution(arr):
    arr.sort(key=lambda x:x[0])
    arr.sort(key=lambda x:x[1])
    answer = 1
    s = arr[0][1]
    for j in range(1, len(arr)):
        if s <= arr[j][0]:
            answer += 1
            s = arr[j][1]
    return answer
            
if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(solution(arr))