def solution(x:int=1):
    if x <= 1:
        return 1
    return solution(x-1) * x
if __name__ == "__main__":
    x = input()
    print(solution(int(x)))