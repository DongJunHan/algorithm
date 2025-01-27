import sys

def solution(sum: int)-> int:
    a = [0,1,2,3,4,5,6,7,8,9]
    increase = 0
    while True:
        s = 0
        increase += 1
        if increase >= sum:
            break
        q = increase
        for i in range(6):
            u = int(q / 10)
            r = int(q % 10)
            if u == 0 and r == 0:
                break
            s += r
            q = u
            
        if increase + s == sum:
            return increase
    return 0

if __name__ == "__main__":
    sum = int(input().strip())

    initial = solution(sum=sum)
    print(initial)