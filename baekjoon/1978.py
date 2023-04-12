import math
def solution():
    cnt = input()
    cnt = int(cnt)
    nums = input()
    nums_arr = nums.split()
    for i in range(len(nums_arr)):
        nums_arr[i] = int(nums_arr[i])
    #sort
    nums_arr.sort()
    max_sqrt = math.ceil(math.sqrt(nums_arr[len(nums_arr)-1]))
    print(max_sqrt)
    # temp_arr = [i for i in range(1,1001)]
    if 1 in nums_arr:
        nums_arr.remove(1)
    i = 0
    while True:
        if i >= len(nums_arr):
            break
        if nums_arr[i] != 2 and nums_arr[i] % 2 == 0:
            nums_arr.remove(nums_arr[i])
        else:
            i += 1
    i = 0
    j = 3
    while True:
        if max_sqrt < j:
            break
        if i >= len(nums_arr):
            if len(nums_arr) == 0:
                break
            i = 0
            j += 2
        if nums_arr[i] != j and nums_arr[i] % j == 0:
            nums_arr.remove(nums_arr[i])
        else:
            i += 1
    return len(nums_arr)

if __name__ == "__main__":
    print(solution())