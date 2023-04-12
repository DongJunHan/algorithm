def solution():
    a = input()
    index = 0
    sum = 1
    interval = 6
    while True:
        if sum > int(a):
            index += 1
            return index
        else:
            index += 1
            sum = sum + (interval * index)
if __name__ == "__main__":
    print(solution())