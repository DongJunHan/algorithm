from sys import stdin
class Queue:
    def push(self, num:str, queue:list):
        queue.append(num)
        return queue
    
    def pop(self, queue:list):
        length = len(queue)
        copy_queue = []
        num = -1
        if length > 0:
            num = queue[0]
            for i in range(1, length):
                copy_queue.append(queue[i])
        return num, copy_queue
    
    def size(self, queue:list):
        return len(queue)
    
    def empty(self, queue:list):
        if len(queue) == 0:
            return 1
        else:
            return 0
    
    def front(self, queue:list):
        length = len(queue)
        num = -1
        if length > 0:
            num = queue[0]
        return num
    
    def back(self, queue:list):
        length = len(queue)
        num = -1
        if length > 0:
            num = queue[length - 1]
        return num

if __name__ == "__main__":
    a = input()
    q = Queue()
    queue = []
    for i in range(int(a)):
        line = list(map(str, stdin.readline().split()))
        if "push" in line[0]:
            q.push(line[1], queue)
        elif "pop" in line[0]:
            num, queue = q.pop(queue)
            print(num)
        elif "size" in line[0]:
            print(q.size(queue))
        elif "empty" in line[0]:
            print(q.empty(queue))
        elif "front" in line[0]:
            print(q.front(queue))
        elif "back" in line[0]:
            print(q.back(queue))