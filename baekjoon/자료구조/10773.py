from sys import stdin
def solution(cnt:int):
    answer = 0
    stack = []
    for i in range(cnt):
        num = int(stdin.readline())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    for i in stack:
        answer += i
    return answer

if __name__ == "__main__":
    num = input()
    print(solution(int(num)))