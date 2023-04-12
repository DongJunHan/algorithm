import math
def solution():
    a = input()
    arr = a.split()
    arr[0] = int(arr[0])
    arr[1] = int(arr[1])
    arr.sort()
    input_arr = [x for x in range(0,arr[1]+1)]
    max_sqrt = math.ceil(math.sqrt(arr[1]))
    input_arr[1] = 0
    for i in range(2,max_sqrt+1):
        if input_arr[i] == 0:
            continue
        for j in range(i*2,len(input_arr),i):
            input_arr[j] = 0

    for k in input_arr[arr[0]:]:
        if k != 0:
            print(k)

if __name__ == "__main__":
    solution()