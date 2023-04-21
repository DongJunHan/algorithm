def solution(s):
    answer = []
    zero_cnt = 0
    binary_cnt = 0
    while s != "1":
        arr = s.split("0")
        zero_cnt += len(arr)-1
        dex = str(len("".join(arr)))
        s = binary_convert(dex)
        binary_cnt += 1
    return [binary_cnt, zero_cnt]


def binary_convert(x:str)->str:
    num = int(x)
    ret = ""
    while num != 0:
        ret = str(num % 2) + ret
        num = num // 2
    return ret





if __name__ == "__main__":
    # s = "110010101001"
    # s = "01110"
    s = "1111111"
    ret = solution(s)
    print(f"ret={ret}")