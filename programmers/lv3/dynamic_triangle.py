def solution(triangle):
    answer = 0
    sum_arr = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    while True:
        if sum_arr[0][0] != 0:
            break
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i]) - 1, -1, -1):
                print(f"i: {i}, j:{j}")
                
                sum_arr[i][j] = max(triangle[i + 1][j] + sum_arr[i][j], triangle[i + 1][j+1] + sum_arr[i][j])\
                 + triangle[i][j]
    print(f"sum_arr: {sum_arr}")
    return answer
def dynamic(t, sum_arr, i, j):
    if len(sum_arr) - 1 == i or len(sum_arr[i]) -1 == j:
        return t[i][j]
    if sum_arr[i][j] != 0:
        return sum_arr[i][j]
    print(f"i:{i}, j:{j}")
    s1 = dynamic(t, sum_arr, i+1, j)
    s2 = dynamic(t, sum_arr, i+1, j + 1)
    if s1 > s2:
        sum_arr[i+1][i] = max(s1,s2)
        return sum_arr[i+1][i]
    else:
        sum_arr[i+1][i+1] = max(s1,s2)
        return sum_arr[i+1][i+1]


# import timeit
if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    ret = solution(triangle)
    print(f"ret={ret}")
    # elapsed_time = (timeit.default_timer() - start) * 1000 # 밀리초 단위로 변환
    # print(f"Elapsed time: {elapsed_time} ms, ret={ret}, {memory}")