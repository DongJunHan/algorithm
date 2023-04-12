from math import ceil, sqrt
import sys
from datetime import datetime
def solution():
    """
        10250.py
        1. 입력 값을 받는다.
        2. 입력 값을 배열에 저장 후  오름차순 정렬을 실시한다.
        3. 제일 큰  값을 가지고 소수판을 만든다.
        4. 만든 소수 판을 가지고 재활용하여 차이가 제일 적은 두 소수를 구한다. 
        이 때 차이가 가장 작은 값을 구해야 하므로 앞에서부터(index=0) 순차적으로 할 필요없이 중간서부터 내려온다.
    """
    #1.
    # m = int(sys.stdin.readline().rstrip())
    input_arr = []
    # input_arr = [int(input()) for _ in range(m)]
    start = datetime.now()
    with open("9020.txt", 'r') as f:
        input_arr = f.read().split()
    for i in range(len(input_arr)):
        input_arr[i] = int(input_arr[i].rstrip())
    
    #2.
    max_input = max(input_arr)
    prime_num = [x for x in range(max_input+1)]
    prime_num[1] = 0
    max_sqrt = ceil(sqrt(max_input))

    #3.
    for j in range(2,max_sqrt + 1):
        if prime_num[j] == 0:
            continue
        for k in range(j*2,len(prime_num),j):
            prime_num[k] = 0
    print(prime_num)
    #4.
    for i in range(len(input_arr)):
        for j in range(input_arr[i] // 2 , 1, -1):
            F = input_arr[i] - j
            if prime_num[j] != 0 and prime_num[F] != 0:
                print(str(j) + " " + str(F))
                break
    end = datetime.now()
    print(end.microsecond-start.microsecond)

    
if __name__ == "__main__":
    solution()