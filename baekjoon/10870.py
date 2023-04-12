def solution(x:int=1):
    if x == 1 or x == 2:
        return 1
    elif x == 0:
        return 0
    return solution(x - 1) + solution(x - 2)
if __name__ == "__main__":
    x = input()
    print(solution(int(x)))