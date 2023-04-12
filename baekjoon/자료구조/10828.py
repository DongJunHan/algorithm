import sys

class Stack:
    def push(self,number:str, stack:list):
        stack.append(number)
        return stack
    def pop(self, stack:list):
        length = len(stack)
        result = None
        if length == 0:
            result = "-1"
        else:
            result = stack.pop()
        return result, stack
    def top(self,stack:list):
        length = len(stack)
        if length == 0:
            result = "-1"
        else:
            result = stack[length-1]
        return result
    def size(self, stack:list):
        result = len(stack)
        return result
    def empty(self, stack:list):
        length = len(stack)
        if length == 0:
            result = "1"
        else:
            result = "0"
        return result

if __name__ == "__main__":
    a = input()
    stack = []
    result = ""
    s = Stack()
    for i in range(int(a)):
        order = list(map(str, sys.stdin.readline().split()))
        if "push" in order[0]:
            stack = s.push(order[1], stack)
        elif "pop" in order[0]:
            result, stack = s.pop(stack)
            print(result)
        elif "size" in order[0]:
            result = s.size(stack)
            print(result)
        elif "empty" in order[0]:
            result = s.empty(stack)
            print(result)
        elif "top" in order[0]:
            result = s.top(stack)
            print(result)
