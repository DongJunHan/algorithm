def solution(s):
    answer = True
    is_pair = 0
    for i in s:
        if i == "(":
            is_pair += 1
        elif i == ")":
            if is_pair > 0:
                is_pair -= 1
            else:
                answer = False
                break
    if  is_pair > 0:
        answer = False
    return answer


if __name__ == "__main__":
    s = "()()"
    # s = "(())()"
    # s = ")()("
    # s = "((())()"
    # s = "(()("
    ret = solution(s)
    print(f"ret={ret}")