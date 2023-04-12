def solution(N:int=3, K:int=1, start:int=1, destination:int=3, current_count:int=0):
    """
        하노이 탑 K
    """
    if N == 1:
        current_count += 1
        # print(f"11 N: {N}, start: {start}, destination: {destination}, current_count: {current_count}")
        if current_count == K:
            print(str(start)+" "+str(destination))
            exit(0)
        return current_count
    next_destination = 6 - (start + destination)
    current_count = solution(N - 1, K, start, next_destination, current_count)
    current_count += 1
    # print(f"22 N: {N}, start: {start}, destination: {destination}, current_count: {current_count}")
    if current_count == K:
        print(str(start)+" "+str(destination))
        exit(0)
    current_count = solution(N - 1, K, next_destination, destination, current_count)
    # print(f"33 N: {N}, start: {start}, destination: {destination}, current_count: {current_count}")
    return current_count

if __name__ == "__main__":
    a = input()
    arr = a.split()
    for i in range(int(arr[0]), 0, -1):
        # print(f"pow: {pow(2,i) - 1}, K : {arr[1]}")
        if (pow(2,i) - 1) <= int(arr[1]):
            arr[0] = i + 1
            break
    solution(arr[0], int(arr[1]))
