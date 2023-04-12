def solution():
    a = input()
    arr = a.split()
    if (int(arr[2]) - int(arr[1])) < 0:
        return -1
    return (int(arr[0]) // (int(arr[2]) - int(arr[1]))) + 1

if __name__ == "__main__":
   print(solution())