from math import sqrt,ceil
import sys
def solution():
    # with open("4948.txt", 'r') as f:
        # arr = f.read().split("\n")
    arr = []
    while True:
        a = input()
        arr.append(a)
        if a == '0':
            break
    answer = []
    for n in range(len(arr)-1):
        cnt = 0
        arr[n] = int(arr[n].strip())
        num_arr = [x for x in range(0,2*arr[n]+1)]
        num_arr[1] = 0
        max_sqrt = ceil(sqrt(num_arr[len(num_arr)-1]))
        for i in range(2, max_sqrt+1):
            if num_arr[i] == 0:
                continue
            for j in range(i*2,len(num_arr),i):
                num_arr[j] = 0
        for k in num_arr[arr[n]+1:]:
            if k != 0:
                cnt += 1
        answer.append(cnt)
    for i in answer:
        print(i)
if __name__ == "__main__":
    solution()