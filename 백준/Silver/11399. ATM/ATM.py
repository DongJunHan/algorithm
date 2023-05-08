def solution(arr):
    arr.sort()
    s = 0
    for i in range(len(arr)):
        s = s + arr[i]
        arr[i] = s
        
    return sum(arr)

if __name__ == "__main__":
    N = input()
    s = input()
    arr = s.split(" ")
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    ret = solution(arr)
    print(ret)