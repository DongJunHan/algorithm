def solution():
    """
        big num A + B
        Step1. Reverse input number
        Step2. Fill '0'
        Step3. Calculator numbers
        Step4. add cherrysum
    """
    num = input()
    arr = num.split()
    arr[0] = arr[0][:None:-1]
    arr[1] = arr[1][:None:-1]
    answer = ''
    if len(arr[0]) > len(arr[1]):
        length = len(arr[0])
        for i in range(length-len(arr[1])):
            arr[1] += '0'
    elif len(arr[0]) < len(arr[1]):
        length = len(arr[1])
        for i in range(length-len(arr[0])):
            arr[0] += '0'
    else:
        length = len(arr[0])
    cheerysum = 0
    for i in range(length):
        sum_ = int(arr[0][i]) + int(arr[1][i]) + cheerysum
        cheerysum = sum_ // 10
        answer += str(sum_ % 10)
    
    if cheerysum == 1:
        answer += '1'

    return answer[:None:-1]
if __name__ == "__main__":
    print(solution())