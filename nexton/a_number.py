def solution(x: int= 1)->int:
    """
        0보다 큰 정수 k자리수 x에 대해 x 제곱에 마지막 k자리수가 x와 동일하면 1 아니면 0을 반환.
        0 < x < 2147473647
        my idea:
        1. string타입으로 변경
        2. reverse
        3. 자리수 문제로 0을 더함.
        solution:
        1. 마지막 k자리수가 자신일려면 x * (x-1)이 k자리수 만큼 0이어야 한다. 즉 10의 제곱근 625기준으로는 625 * 624 = 390000
        2. 10의 배수라면 (2*5)^n이어야하는데 둘 중 하나는 5의 배수여야하고, 나머지는 5의배수는 아니고 2의 배수여아한다.
    """
    answer = -1
    str_x = str(x)
    str_x = str_x[:None:-1]
    # str_x2 = str_x
    # tmp1 = []
    # tmp2 = []
    # for i in range(len(str_x)):
    #     r = 0
    #     l = len(str_x)+i
    #     for j in range(l):
    #         if l - len(str_x) >= l-j:
    #             tmp1.append('0')
    #         else:
    #             r = int(str_x[j]) * int(str_x[i] + r) // 10
    #             z = str(int(str_x[j]) * int(str_x[i] + r) % 10)
    #             tmp1.append(z)
        
    return answer
if __name__ == "__main__":
    x = 625
    solution(x)