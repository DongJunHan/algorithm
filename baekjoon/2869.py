import math
def solution():
    h = input()
    arr = h.split()
    a = int(arr[0])
    b = int(arr[1])
    v = int(arr[2])
    r = v - a
    gr = r / (a-b)
    return math.ceil(gr) + 1


if __name__ == "__main__":
    print(solution())