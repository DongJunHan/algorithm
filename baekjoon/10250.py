import math
def solution():
    length = input()
    answer = []
    #input test case
    for i in range(0,int(length)):
        a = input()
        b = a.split()
        print(b)
        b[0] = int(b[0])
        b[1] = int(b[1])
        b[2] = int(b[2])
        divide = math.ceil(b[2] / b[0]) - 1
        
        c = b[2] - (b[0]*divide)
        answer.append('%d%02d'%(c,1+divide))
    
    return answer
if __name__ == "__main__":
    answer = solution()
    for i in answer:
        print(i)