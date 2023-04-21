def solution(s):
    answer = True
    close_list = []
    for i in s:
        if i == "(":
            close_list.append(True)
        elif i == ")":
            if len(close_list) > 0:
                close_list.pop()
            else:
                answer = False
                break
    if len(close_list) > 0:
        answer = False
    return answer


if __name__ == "__main__":
    # s = "()()"
    # s = "(())()"
    # s = ")()("
    s = "((())()"
    # s = "(()("
    ret = solution(s)
    print(f"ret={ret}")