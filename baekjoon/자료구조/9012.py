def solution():
    """
        1. 처음 생각해낸 아이디어는 여는괄호'('가 나오면 카운트를 세고, 닫는괄호')'가 나오면 그것도 카운트를 센 뒤, 
        그 둘의 빼서 0이면 쌍이 다 맞는 것으로 알고리즘을 짰다. 
            문제 발생: 닫는괄호 ')'가 먼저 나오는 것을 걸러내지 못함. 그리고 닫는괄호랑 여는괄호의 쌍이 무조건 맞으면 True였기 때문에 ())(() 를 걸러내지못함
        2. 스택에 여는괄호'('나오면 넣고 닫는괄호 ')' 나오면 빼는 식으로 변경. 닫는괄호 ')'먼저 나오면 스택에 남아있는 요소가 있으면 진행시고 아니면 그 자리에서 멈추는식.
        3. 1번에서 카운트하는 방법을 2번처럼 여는괄호 나오면 더하고 닫는괄호 나오면 빼는식으로 해도 되지 않을까?
    """
    cnt = input()
    answer = []
    for i in range(int(cnt)):
        a = input()
        arr = []
        length = len(a)
        count = 0
        for i in range(length):
            if a[i] == "(":
                count += 1
            elif a[i] == ")":
                if count == 0:
                    count += 1
                    break
                count -= 1
            # if a[i] == "(":
            #     arr.append("(")
            # elif a[i] == ")":
            #     if len(arr) == 0:
            #         arr.append("(")
            #         break
            #     arr.pop()
        # if len(arr) == 0:
        if count == 0:
            answer.append("YES")
        else:
            answer.append("NO")
    return answer
if __name__ == "__main__":
    answer = solution()
    for i in answer:
        print(i)