import math
def solution():
    a = input()
    a = int(a)
    origin = a
    arr = []
    prime_num = [2,3]
    i = 0
    j = 3
    while True:
        if a % 2 != 0:
            break
        a = a // 2
        arr.append(2)
    while True:
        if j > origin:
            break
        if a == 1:
            break
        if a % j != 0:
            j += 2
            if a % j != 0:
                continue    
        a = a // j
        arr.append(j)
    return arr
if __name__ == "__main__":
    arr = solution()
    for i in arr:
        print(i)