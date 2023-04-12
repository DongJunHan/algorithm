def solution(x:int=1, start:int=1, destination:int=3):
    if x == 1:
        print(str(start) + " " + str(destination))
        return
    next_destinamtion = 6 - (start + destination)
    solution(x - 1, start, next_destinamtion)
    print(str(start) + " " + str(destination))
    solution(x - 1, next_destinamtion, destination)
    
if __name__ == "__main__":
    x = input()
    print(pow(2,int(x))-1)
    solution(int(x))