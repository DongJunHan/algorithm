def solution(common):
    answer = 0
    # 조건에 의해서 2개의 데이터만 주어지는 경우가 있음
    if len(common) == 2:
        return common[1] + (common[1] - common[0])

    #등차인지 등비인지부터 알아내보자.
    arr = []
    for i in range(0,2):
        arr.append(common[i+1] - common[i])
    if arr[0] == arr[1]:#등차
        return common[len(common)-1] + arr[0]
    else:
        return common[len(common)-1] * (common[1] // common[0])
        
    

if __name__ == "__main__":
    # common = [1, 2, 3, 4]
    common = [2,4,8]
    ret = solution(common)
    print(f"ret={ret}")