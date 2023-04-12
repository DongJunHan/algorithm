import math
def solution():
    m = input()
    n = input()
    arr = [x for x in range(int(m),int(n)+1)]
    max_sqrt = math.ceil(math.sqrt(arr[len(arr)-1]))
    if 1 in arr:
        arr.remove(1)
    
    i = 0
    while True:
        if i >= len(arr):
            i = 0
            break
        if arr[i] != 2 and arr[i] % 2 == 0:
            arr.remove(arr[i])
        i += 1
    j = 3
    while True:
        if max_sqrt < j:
            break
        if i >= len(arr):
            if len(arr) == 0:
                break
            i = 0
            j += 2
        if arr[i] != j and arr[i] % j == 0:
            arr.remove(arr[i])
        else:
            i += 1
    sum_ = 0
    for k in arr:
        sum_ += k
    if len(arr) == 0:
        minimum = -1
    else:
        minimum = arr[0]
    return sum_, minimum
if __name__ == "__main__":
    sum_ , minimum = solution()
    if minimum > -1:
        print(sum_)
    print(minimum)