import sys
# from datetime import datetime
def solution():
    first_num = int(sys.stdin.readline().strip())
    # first_input = [i for i in range(1,50000)]
    first_input = list(map(int, sys.stdin.readline().split()))
    second_num = int(sys.stdin.readline().strip())
    # second_input = [i for i in range(1,100000,2)]
    second_input = list(map(int, sys.stdin.readline().split()))
    # start_time = datetime.now()
    second_length = len(second_input)
    first_length = len(first_input)
    first_input.sort()
    half = first_length // 2 + 1
    print_result = ""
    for i in range(second_length):
        start = 0
        end = first_length - 1
        result = None
        while start <= end:
            mid = (start + end) // 2 
            # print(f"first mid: {mid}, value: {first_input[mid]}, second: {second_input[i]}")
            if second_input[i] == first_input[mid]:
                result = "1"
                break
            if second_input[i] < first_input[mid]:
                end = mid - 1
            else:
                start = mid + 1
        if result is None:
            print_result += "0"
        else:
            print_result += "1"
        if i != second_length - 1:
            print_result += "\n"
    print(print_result)
    # end_time = datetime.now()
    # print(end_time - start_time)

if __name__ == "__main__":
    solution()