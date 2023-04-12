from collections import deque
from itertools import permutations
def solution(expression):
    opts = ["+","*","-"]
    answer = 0
    #create stack
    ls = []
    start_index = 0
    for i, txt in enumerate(expression):
        if txt in opts:
            ls.append(expression[start_index:i])
            ls.append(txt)
            start_index = i + 1
    else:
        ls.append(expression[start_index:])
    print(ls)
    #사용하지 않은 연산자 삭제
    for op in opts:
        if op not in expression:
            opts.remove(op)
    
    #opt에 있는 연산자로 구성할 수 있는 모든 우선순위 생성
    primarity = permutations(opts)
    for case in primarity:
        print(case)
        stacks = [deque(ls),deque()]
        t1 = 1
        #연산자별 케이스 맨 앞에 나오는 연산자가 당연히 우선순위가 높다
        for c in case:
            t1 = (t1+1) % 2 # 스택 토글 변수
            t2 = (t1+1) % 2
            #스택에 값이 없을 때까지 돌린다.
            while len(stacks[t1]):
                item = stacks[t1].popleft()
                #비어있는 스택2에 값이 없으면 조건문을 지나서 값을 넣고,
                #스택2에 비어있지 않고, 해당 값이 현재 돌고있는 연산자와 같다면
                # 숫자를 꺼내서 연산을 수행(eval)을 함.
                if len(stacks[t2]) and stacks[t2][-1] == c:
                    c = stacks[t2].pop()
                    n = stacks[t2].pop()
                    item = str(eval(str(n)+c+str(item)))

                stacks[t2].append(item)
            
        result = stacks[len(opts)%2].pop()
        result = abs(int(result))
        answer = max(answer, result)
    return answer  
if __name__ == "__main__":
    expression = "100-200*300-500+20"
    # expression = "50*6-3*2"
    print(solution(expression))