import math
def solution():
    a = input()
    x = 1
    b = 0
    sum_ = 1
    mom = 0
    sun = 0
    while True:
        if sum_ >= int(a):
            b = sum_ - int(a)
            if sum_ == 1:
                return "1/1"
            if x % 2 == 0:
                sun = x - b
                mom = 1 + b
            else:
                mom = x - b
                sun = 1 + b
            return str(sun)+"/"+str(mom)
        x += 1
        sum_ = x + sum_

if __name__ == "__main__":
    print(solution())